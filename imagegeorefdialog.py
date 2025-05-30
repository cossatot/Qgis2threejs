# -*- coding: utf-8 -*-
# (C) 2023
# SPDX-License-Identifier: GPL-2.0-or-later

import os
import json
import numpy as np

from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QImage, QPixmap, QGuiApplication, QPolygonF, QColor
from PyQt5.QtWidgets import (QDialog, QFileDialog, QGraphicsScene, 
                           QGraphicsPolygonItem, QGraphicsPixmapItem,
                           QMessageBox, QVBoxLayout, QHBoxLayout, QGridLayout,
                           QLabel, QLineEdit, QPushButton, QGroupBox, 
                           QGraphicsView, QDialogButtonBox)

from qgis.core import QgsPointXY, QgsProject, QgsCoordinateTransform, QgsGeometry, QgsRectangle
from qgis.gui import QgsMapToolEmitPoint, QgsMapCanvas

class ImageGeorefDialog(QDialog):
    """Dialog for georeferencing images for 3D display in Qgis2threejs."""
    
    def __init__(self, parent, iface):
        super().__init__(parent)
        self.iface = iface
        self.mapCanvas = iface.mapCanvas()
        self.setupUI()
        
        # Initialize variables
        self.imagePath = ""
        self.image = None
        self.mapTool = None
        self.activeCorner = None
        self.corners = {}  # Will store corner coordinates
        
        # Set up the graphics scene for preview
        self.scene = QGraphicsScene()
        self.graphicsView_Preview.setScene(self.scene)
        
        # Connect signals
        self.pushButton_Browse.clicked.connect(self.browseImage)
        self.pushButton_LoadGeoJSON.clicked.connect(self.loadFromGeoJSON)
        self.pushButton_Map1.clicked.connect(lambda: self.activateMapTool(1))
        self.pushButton_Map2.clicked.connect(lambda: self.activateMapTool(2))
        self.pushButton_Map3.clicked.connect(lambda: self.activateMapTool(3))
        self.pushButton_Map4.clicked.connect(lambda: self.activateMapTool(4))
        
        # Connect coordinate text edits to update preview
        self.lineEdit_X1.textChanged.connect(self.updatePreview)
        self.lineEdit_Y1.textChanged.connect(self.updatePreview)
        self.lineEdit_Z1.textChanged.connect(self.updatePreview)
        self.lineEdit_X2.textChanged.connect(self.updatePreview)
        self.lineEdit_Y2.textChanged.connect(self.updatePreview)
        self.lineEdit_Z2.textChanged.connect(self.updatePreview)
        self.lineEdit_X3.textChanged.connect(self.updatePreview)
        self.lineEdit_Y3.textChanged.connect(self.updatePreview)
        self.lineEdit_X4.textChanged.connect(self.updatePreview)
        self.lineEdit_Y4.textChanged.connect(self.updatePreview)
        self.lineEdit_Z4.textChanged.connect(self.updatePreview)
    
    def setupUI(self):
        """Create the UI without using .ui file"""
        self.setWindowTitle("Georeferenced Image")
        self.resize(640, 520)
        
        # Main layout
        main_layout = QVBoxLayout(self)
        
        # Image group
        group_image = QGroupBox("Image")
        image_layout = QHBoxLayout(group_image)
        
        label_file = QLabel("File:")
        self.lineEdit_ImageFile = QLineEdit()
        self.pushButton_Browse = QPushButton("Browse...")
        
        image_layout.addWidget(label_file)
        image_layout.addWidget(self.lineEdit_ImageFile)
        image_layout.addWidget(self.pushButton_Browse)
        
        # Preview group
        group_preview = QGroupBox("Preview")
        preview_layout = QVBoxLayout(group_preview)
        
        self.graphicsView_Preview = QGraphicsView()
        preview_layout.addWidget(self.graphicsView_Preview)
        
        # Corners group
        group_corners = QGroupBox("Corner Coordinates (in project CRS)")
        corners_layout = QGridLayout(group_corners)
        
        # Add GeoJSON import button
        self.pushButton_LoadGeoJSON = QPushButton("Load from GeoJSON")
        corners_layout.addWidget(self.pushButton_LoadGeoJSON, 0, 0, 1, 5)
        
        # Top-Left corner
        label_topLeft = QLabel("Top-Left:")
        self.lineEdit_X1 = QLineEdit()
        self.lineEdit_X1.setPlaceholderText("X")
        self.lineEdit_Y1 = QLineEdit()
        self.lineEdit_Y1.setPlaceholderText("Y")
        self.lineEdit_Z1 = QLineEdit()
        self.lineEdit_Z1.setPlaceholderText("Z")
        self.pushButton_Map1 = QPushButton("Map")
        
        corners_layout.addWidget(label_topLeft, 1, 0)
        corners_layout.addWidget(self.lineEdit_X1, 1, 1)
        corners_layout.addWidget(self.lineEdit_Y1, 1, 2)
        corners_layout.addWidget(self.lineEdit_Z1, 1, 3)
        corners_layout.addWidget(self.pushButton_Map1, 1, 4)
        
        # Top-Right corner
        label_topRight = QLabel("Top-Right:")
        self.lineEdit_X2 = QLineEdit()
        self.lineEdit_X2.setPlaceholderText("X")
        self.lineEdit_Y2 = QLineEdit()
        self.lineEdit_Y2.setPlaceholderText("Y")
        self.lineEdit_Z2 = QLineEdit()
        self.lineEdit_Z2.setPlaceholderText("Z")
        self.pushButton_Map2 = QPushButton("Map")
        
        corners_layout.addWidget(label_topRight, 2, 0)
        corners_layout.addWidget(self.lineEdit_X2, 2, 1)
        corners_layout.addWidget(self.lineEdit_Y2, 2, 2)
        corners_layout.addWidget(self.lineEdit_Z2, 2, 3)
        corners_layout.addWidget(self.pushButton_Map2, 2, 4)
        
        # Bottom-Right corner
        label_bottomRight = QLabel("Bottom-Right:")
        self.lineEdit_X3 = QLineEdit()
        self.lineEdit_X3.setPlaceholderText("X")
        self.lineEdit_Y3 = QLineEdit()
        self.lineEdit_Y3.setPlaceholderText("Y")
        self.lineEdit_Z3 = QLineEdit()
        self.lineEdit_Z3.setPlaceholderText("Z")
        self.pushButton_Map3 = QPushButton("Map")
        
        corners_layout.addWidget(label_bottomRight, 3, 0)
        corners_layout.addWidget(self.lineEdit_X3, 3, 1)
        corners_layout.addWidget(self.lineEdit_Y3, 3, 2)
        corners_layout.addWidget(self.lineEdit_Z3, 3, 3)
        corners_layout.addWidget(self.pushButton_Map3, 3, 4)
        
        # Bottom-Left corner
        label_bottomLeft = QLabel("Bottom-Left:")
        self.lineEdit_X4 = QLineEdit()
        self.lineEdit_X4.setPlaceholderText("X")
        self.lineEdit_Y4 = QLineEdit()
        self.lineEdit_Y4.setPlaceholderText("Y")
        self.lineEdit_Z4 = QLineEdit()
        self.lineEdit_Z4.setPlaceholderText("Z")
        self.pushButton_Map4 = QPushButton("Map")
        
        corners_layout.addWidget(label_bottomLeft, 4, 0)
        corners_layout.addWidget(self.lineEdit_X4, 4, 1)
        corners_layout.addWidget(self.lineEdit_Y4, 4, 2)
        corners_layout.addWidget(self.lineEdit_Z4, 4, 3)
        corners_layout.addWidget(self.pushButton_Map4, 4, 4)
        
        # Button box
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        # Add all widgets to main layout
        main_layout.addWidget(group_image)
        main_layout.addWidget(group_preview)
        main_layout.addWidget(group_corners)
        main_layout.addWidget(self.buttonBox)
    
    def browseImage(self):
        """Open file dialog to select an image."""
        imagePath, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.tif *.tiff);;All files (*.*)")
        
        if imagePath:
            self.imagePath = imagePath
            self.lineEdit_ImageFile.setText(imagePath)
            self.loadImage(imagePath)
    
    def loadImage(self, path):
        """Load the selected image and display in preview."""
        self.image = QImage(path)
        if self.image.isNull():
            QMessageBox.warning(self, "Error", "Failed to load image.")
            return
        
        # Display image in preview
        pixmap = QPixmap.fromImage(self.image)
        self.scene.clear()
        self.scene.addPixmap(pixmap)
        self.graphicsView_Preview.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
    
    def activateMapTool(self, cornerNum):
        """Activate map tool to pick coordinates from map canvas."""
        self.activeCorner = cornerNum
        
        # Deactivate previous map tool if any
        if self.mapTool:
            self.mapCanvas.unsetMapTool(self.mapTool)
        
        # Create and set new map tool
        self.mapTool = QgsMapToolEmitPoint(self.mapCanvas)
        self.mapTool.canvasClicked.connect(self.mapClicked)
        self.mapCanvas.setMapTool(self.mapTool)
        
        # Minimize dialog while map tool is active
        self.setWindowState(Qt.WindowMinimized)
    
    def mapClicked(self, point, button):
        """Handle map canvas click to set corner coordinates."""
        if button != Qt.LeftButton or self.activeCorner is None:
            return
        
        # Get z value from the current field
        z_field = getattr(self, f"lineEdit_Z{self.activeCorner}")
        z_value = z_field.text()
        z = float(z_value) if z_value else 0.0
        
        # Set the coordinates in the input fields
        getattr(self, f"lineEdit_X{self.activeCorner}").setText(str(point.x()))
        getattr(self, f"lineEdit_Y{self.activeCorner}").setText(str(point.y()))
        
        # Store corner in our dictionary
        self.corners[self.activeCorner] = (point.x(), point.y(), z)
        
        # Reset map tool and restore window
        self.mapCanvas.unsetMapTool(self.mapTool)
        self.mapTool = None
        self.activeCorner = None
        self.setWindowState(Qt.WindowActive)
        
        # Update preview
        self.updatePreview()
    
    def updatePreview(self):
        """Update the preview with current corner coordinates."""
        if not self.image or self.image.isNull():
            return
        
        # Check if we have all coordinates
        have_all_coords = True
        polygon_points = QPolygonF()
        
        for i in range(1, 5):
            x_field = getattr(self, f"lineEdit_X{i}")
            y_field = getattr(self, f"lineEdit_Y{i}")
            
            if not x_field.text() or not y_field.text():
                have_all_coords = False
                break
            
            # Get image coordinates (normalized 0-1)
            img_x = 0 if i in [1, 4] else 1  # Left or right
            img_y = 0 if i in [1, 2] else 1  # Top or bottom
            
            # Map to scene coordinates
            scene_x = img_x * self.image.width()
            scene_y = img_y * self.image.height()
            
            polygon_points.append(QPointF(scene_x, scene_y))
        
        # If we have all coordinates, draw the polygon
        if have_all_coords:
            # Redraw the scene
            self.scene.clear()
            pixmap_item = QGraphicsPixmapItem(QPixmap.fromImage(self.image))
            self.scene.addItem(pixmap_item)
            
            # Add polygon outline
            polygon_item = QGraphicsPolygonItem(polygon_points)
            polygon_item.setPen(Qt.red)
            self.scene.addItem(polygon_item)
            
            self.graphicsView_Preview.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
    
    def getCornerCoordinates(self):
        """Return the corner coordinates as a list of (x,y,z) tuples."""
        corners = []
        for i in range(1, 5):
            x_field = getattr(self, f"lineEdit_X{i}")
            y_field = getattr(self, f"lineEdit_Y{i}")
            z_field = getattr(self, f"lineEdit_Z{i}")
            
            try:
                x = float(x_field.text())
                y = float(y_field.text())
                z = float(z_field.text()) if z_field.text() else 0.0
                corners.append((x, y, z))
            except ValueError:
                return None
        
        return corners
    
    def accept(self):
        """Called when OK button is clicked."""
        # Validate inputs
        if not self.imagePath:
            QMessageBox.warning(self, "Error", "Please select an image.")
            return
        
        corners = self.getCornerCoordinates()
        if not corners or len(corners) != 4:
            QMessageBox.warning(self, "Error", "Please set all corner coordinates.")
            return
        
        super().accept()
    
    def loadFromGeoJSON(self):
        """Load polygon corners from a GeoJSON file."""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select GeoJSON File", "", "GeoJSON Files (*.geojson *.json);;All files (*.*)")
        
        if not file_path:
            return
        
        try:
            # Load GeoJSON file
            with open(file_path, 'r') as f:
                geojson_data = json.load(f)
            
            # Find first polygon feature
            polygon_coords = None
            is_3d_geojson = False
            
            # Process features
            for feature in geojson_data.get('features', []):
                geometry = feature.get('geometry', {})
                if geometry.get('type') == 'Polygon':
                    # Get exterior ring (first ring)
                    polygon_coords = geometry.get('coordinates', [[]])[0]
                    # Check if it's 3D coordinates
                    if polygon_coords and len(polygon_coords[0]) >= 3:
                        is_3d_geojson = True
                    break
            
            # If no polygon found in features, check if this is a direct geometry
            if polygon_coords is None and geojson_data.get('type') == 'Polygon':
                polygon_coords = geojson_data.get('coordinates', [[]])[0]
                # Check if it's 3D coordinates
                if polygon_coords and len(polygon_coords[0]) >= 3:
                    is_3d_geojson = True
            
            if not polygon_coords or len(polygon_coords) < 4:
                QMessageBox.warning(self, "Error", "No valid polygon found in GeoJSON file or polygon has fewer than 4 vertices.")
                return
            
            # Use the actual points from the polygon - first 4 points
            # Just take the coordinates directly as they are in the GeoJSON
            if len(polygon_coords) < 4:
                QMessageBox.warning(self, "Error", "The polygon needs at least 4 points.")
                return
                
            # Take the first 4 points directly
            corners = []
            for i in range(4):
                coord = polygon_coords[i]
                if is_3d_geojson and len(coord) >= 3:
                    # Use the Z coordinate if it exists
                    corners.append((coord[0], coord[1], coord[2]))
                else:
                    # Otherwise use 0.0 as Z
                    corners.append((coord[0], coord[1], 0.0))
            
            # Update UI fields and store corners
            for i, (x, y, z) in enumerate(corners):
                corner_idx = i + 1
                getattr(self, f"lineEdit_X{corner_idx}").setText(str(x))
                getattr(self, f"lineEdit_Y{corner_idx}").setText(str(y))
                getattr(self, f"lineEdit_Z{corner_idx}").setText(str(z))
                
                # Store corner
                self.corners[corner_idx] = (x, y, z)
            
            # Update preview
            self.updatePreview()
            
            # Create simple success message
            msg = f"Loaded coordinates directly from GeoJSON file.\n\n"
            if is_3d_geojson:
                msg += "Z values were preserved from the 3D GeoJSON data.\n\n"
            msg += "The first 4 points of the polygon are used as corners."
            
            QMessageBox.information(self, "Success", msg)
            
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to parse GeoJSON file: {str(e)}")
    
    def getImageData(self):
        """Return the image path and corner coordinates."""
        return {
            "path": self.imagePath,
            "corners": self.getCornerCoordinates()
        }