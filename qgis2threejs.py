# -*- coding: utf-8 -*-
# (C) 2013 Minoru Akagi
# SPDX-License-Identifier: GPL-2.0-or-later
# begin: 2013-12-21

import os

from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QAction, QActionGroup, QMenu
from PyQt5.QtGui import QIcon
from qgis.core import QgsApplication, QgsProject, QgsPointXY, QgsGeometry, QgsFeature, QgsVectorLayer

from .conf import DEBUG_MODE, PLUGIN_NAME
from .exportsettings import ExportSettings
from .procprovider import Qgis2threejsProvider
from .utils import logMessage, pluginDir, removeTemporaryOutputDir, settingsFilePath
from .q3dwindow import Q3DWindow
from .q3dview import WEBENGINE_AVAILABLE, WEBKIT_AVAILABLE, WEBVIEWTYPE_NONE, WEBVIEWTYPE_WEBKIT, WEBVIEWTYPE_WEBENGINE, currentWebViewType
from .imagegeorefdialog import ImageGeorefDialog


class Qgis2threejs:

    def __init__(self, iface):
        self.iface = iface
        self.pprovider = Qgis2threejsProvider()

        self.currentProjectPath = ""
        self.exportSettings = None
        self.liveExporter = None
        self.previewEnabled = True      # last preview state

    def initGui(self):
        # add a toolbar button and web menu items
        icon = QIcon(pluginDir("Qgis2threejs.png"))
        title = "Qgis2threejs Exporter"
        wnd = self.iface.mainWindow()
        objName = "Qgis2threejsExporter"

        self.action = QAction(icon, title, wnd)
        self.action.setObjectName(objName)
        self.action.triggered.connect(self.openExporter)

        self.iface.addWebToolBarIcon(self.action)

        self.actionGroup = QActionGroup(wnd)
        self.actionGroup.setObjectName(objName + "Group")

        # Create an action for the georeferencer
        self.actionGeoreferencer = QAction(QIcon(pluginDir("svg/camera.svg")), "Add Georeferenced Image", wnd)
        self.actionGeoreferencer.setObjectName(objName + "Georeferencer")
        self.actionGeoreferencer.triggered.connect(self.openGeoreferencer)

        if WEBENGINE_AVAILABLE:
            self.actionWebEng = QAction(icon, title + " (WebEngine)", self.actionGroup)
            self.actionWebEng.setObjectName(objName + "WebEng")
            self.actionWebEng.triggered.connect(self.openExporterWebEng)

            self.iface.addPluginToWebMenu(PLUGIN_NAME, self.actionWebEng)

        if WEBKIT_AVAILABLE:
            self.actionWebKit = QAction(icon, title + " (WebKit)", self.actionGroup)
            self.actionWebKit.setObjectName(objName + "WebKit")
            self.actionWebKit.triggered.connect(self.openExporterWebKit)

            self.iface.addPluginToWebMenu(PLUGIN_NAME, self.actionWebKit)
            
        # Add georeferencer action to menu
        self.iface.addPluginToWebMenu(PLUGIN_NAME, self.actionGeoreferencer)

        if WEBENGINE_AVAILABLE and WEBKIT_AVAILABLE:
            self.actionWebEng.setCheckable(True)
            self.actionWebKit.setCheckable(True)

            if QSettings().value("/Qgis2threejs/preferWebKit", False):
                self.actionWebKit.setChecked(True)
            else:
                self.actionWebEng.setChecked(True)

        # connect signal-slot
        QgsProject.instance().removeAll.connect(self.allLayersRemoved)

        # register processing provider
        QgsApplication.processingRegistry().addProvider(self.pprovider)

    def unload(self):
        # disconnect signal-slot
        QgsProject.instance().removeAll.disconnect(self.allLayersRemoved)

        # remove the web menu items and icon
        self.action.triggered.disconnect(self.openExporter)
        self.iface.removeWebToolBarIcon(self.action)

        if WEBENGINE_AVAILABLE:
            self.actionWebEng.triggered.disconnect(self.openExporterWebEng)
            self.iface.removePluginWebMenu(PLUGIN_NAME, self.actionWebEng)

        if WEBKIT_AVAILABLE:
            self.actionWebKit.triggered.disconnect(self.openExporterWebKit)
            self.iface.removePluginWebMenu(PLUGIN_NAME, self.actionWebKit)
            
        # remove georeferencer from menu
        self.actionGeoreferencer.triggered.disconnect(self.openGeoreferencer)
        self.iface.removePluginWebMenu(PLUGIN_NAME, self.actionGeoreferencer)

        # remove provider from processing registry
        QgsApplication.processingRegistry().removeProvider(self.pprovider)

        # remove temporary output directory
        removeTemporaryOutputDir()

    def openExporter(self, _=False, webViewType=None):
        """
        webViewType: WEBVIEWTYPE_NONE, WEBVIEWTYPE_WEBKIT, WEBVIEWTYPE_WEBENGINE or None. None means last used web view type.
        """
        if self.liveExporter:
            logMessage("Qgis2threejs Exporter is already open.")
            self.liveExporter.activateWindow()
            return

        layersUpdated = False
        proj_path = QgsProject.instance().fileName()
        if proj_path and proj_path != self.currentProjectPath:
            filepath = settingsFilePath()   # get settings file path for current project
            if os.path.exists(filepath):
                self.exportSettings = ExportSettings()
                self.exportSettings.loadSettingsFromFile(filepath)
                layersUpdated = True

        self.exportSettings = self.exportSettings or ExportSettings()
        if not layersUpdated:
            self.exportSettings.updateLayers()

        self.exportSettings.isPreview = True
        self.exportSettings.setMapSettings(self.iface.mapCanvas().mapSettings())

        self.liveExporter = Q3DWindow(self.iface,
                                      self.exportSettings,
                                      webViewType=webViewType,
                                      previewEnabled=self.previewEnabled)
        self.liveExporter.show()
        self.liveExporter.destroyed.connect(self.exporterDestroyed)

        self.currentProjectPath = proj_path

    def openExporterWebEng(self):
        self.openExporter(webViewType=WEBVIEWTYPE_WEBENGINE)

        QSettings().remove("/Qgis2threejs/preferWebKit")
        self.actionWebEng.setChecked(True)

    def openExporterWebKit(self):
        self.openExporter(webViewType=WEBVIEWTYPE_WEBKIT)

        if WEBENGINE_AVAILABLE:
            QSettings().setValue("/Qgis2threejs/preferWebKit", True)

        self.actionWebKit.setChecked(True)
        
    def openGeoreferencer(self):
        """Open the georeferencer dialog to add a georeferenced image."""
        from PyQt5.QtCore import QVariant
        from qgis.core import QgsField, Qgis, QgsWkbTypes, QgsGeometry, QgsPolygon, QgsPointXY
        
        # Enable debug logging
        from .utils import logMessage
        logMessage("Opening georeferencer dialog")
        
        dialog = ImageGeorefDialog(self.iface.mainWindow(), self.iface)
        if dialog.exec_():
            # Get image data from dialog
            image_data = dialog.getImageData()
            
            # Create a polygon layer for the image
            layer_name = os.path.splitext(os.path.basename(image_data["path"]))[0]
            memory_layer = QgsVectorLayer("Polygon?crs={}".format(self.iface.mapCanvas().mapSettings().destinationCrs().authid()), 
                                         "Georef_Image_" + layer_name, "memory")
            
            # Create a polygon from the 4 corner coordinates
            corners = image_data["corners"]
            if corners and len(corners) == 4:
                print(f"Creating polygon with corners: {corners}")
                
                # Convert corners to QgsPointXY for polygon creation
                # Order: close the ring by adding the first point at the end
                polygon_points = [
                    QgsPointXY(corners[0][0], corners[0][1]),  # Top-left
                    QgsPointXY(corners[1][0], corners[1][1]),  # Top-right
                    QgsPointXY(corners[2][0], corners[2][1]),  # Bottom-right
                    QgsPointXY(corners[3][0], corners[3][1]),  # Bottom-left
                    QgsPointXY(corners[0][0], corners[0][1])   # Close the ring
                ]
                
                # Create polygon geometry
                polygon_geom = QgsGeometry.fromPolygonXY([polygon_points])
                
                # Create feature with the polygon geometry
                feature = QgsFeature()
                feature.setGeometry(polygon_geom)
                
                # Set attributes for the image path
                provider = memory_layer.dataProvider()
                provider.addAttributes([
                    QgsField("image_path", QVariant.String),
                ])
                memory_layer.updateFields()
                
                feature.setAttributes([image_data["path"]])
                
                # Add feature to layer
                provider.addFeatures([feature])
                memory_layer.updateExtents()
                
                # Add layer to project
                QgsProject.instance().addMapLayer(memory_layer)
                
                # Configure the layer for Qgis2threejs
                from .vectorobject import ObjectType, PolygonType
                
                # Open the exporter to set up the layer
                window = self.openExporter()
                if window:
                    # Set up the layer for polygon display with texture
                    controller = window.controller
                    settings = controller.settings
                    
                    # Get the layer
                    layer_id = memory_layer.id()
                    if layer_id in settings.layers:
                        layer_settings = settings.layers[layer_id]
                        
                        # Set appropriate object type
                        # Use standard PolygonType which is better supported
                        layer_settings.properties.objType = "Polygon"
                        
                        # Set polygon to a semi-transparent red for testing
                        layer_settings.properties.color = "0xff0000"
                        layer_settings.properties.opacity = 0.7
                        
                        # Log for debugging
                        from .utils import logMessage
                        logMessage(f"Created polygon layer with image path: {image_data['path']}")
                        
                        # Update layer settings and rebuild scene
                        controller.setLayerProperties(layer_id, layer_settings.properties)
                        window.updateScene()
                        
                        # Show message
                        self.iface.messageBar().pushMessage(
                            "Qgis2threejs", 
                            "Georeferenced image added as polygon. The polygon should be red and semi-transparent.",
                            level=Qgis.Info, 
                            duration=5
                        )

    def exporterDestroyed(self, obj):
        if currentWebViewType != WEBVIEWTYPE_NONE:
            self.previewEnabled = self.liveExporter.controller.enabled      # remember preview state

        if DEBUG_MODE:
            from .debug_utils import logReferenceCount
            logReferenceCount(self.liveExporter)

        self.liveExporter = None

    def allLayersRemoved(self):
        self.currentProjectPath = ""
        self.exportSettings = None
