# -*- coding: utf-8 -*-
# (C) 2014 Minoru Akagi
# SPDX-License-Identifier: GPL-2.0-or-later
# begin: 2014-01-11

from .q3dconst import LayerType, PropertyID as PID
from .propwidget import PropertyWidget, WVT


class ObjectTypeBase:

    experimental = False

    def __init__(self, settings, mtlManager=None):
        self.settings = settings
        self.mtlManager = mtlManager        # material manager needs to be set before calling .material()

    def setupWidgets(self, ppage):
        pass

    def material(self, feat):
        pass

    def geometry(self, feat, geom):
        pass

    def defaultValue(self):
        return float("{0:.3g}".format(self.settings.baseExtent().width() * 0.01))

    def defaultValueZ(self):
        return float("{0:.3g}".format(self.settings.baseExtent().width() * self.settings.mapTo3d().zScale * 0.01))

    @classmethod
    def displayName(cls):
        return tr(cls.name)

    # def layerProperties(self, layer):
    #     return {}


class PointTypeBase(ObjectTypeBase):

    layerType = LayerType.POINT


class LineTypeBase(ObjectTypeBase):

    layerType = LayerType.LINESTRING


class PolygonTypeBase(ObjectTypeBase):

    layerType = LayerType.POLYGON


# Point
class PointBasicTypeBase(PointTypeBase):

    def material(self, feat):
        return {"idx": self.mtlManager.getMeshMaterialIndex(feat.prop(PID.C), feat.prop(PID.OP))}


class PointType(PointTypeBase):

    name = "Point"
    pids = [PID.C, PID.OP, PID.M0]

    def setupWidgets(self, ppage):
        ppage.setupWidgets(mtlItems=[{"name": "Size", "defVal": 1}])

    def material(self, feat):
        return {"idx": self.mtlManager.getPointMaterialIndex(feat.prop(PID.C), feat.prop(PID.OP), feat.prop(PID.M0))}

    def geometry(self, feat, geom):
        v = []
        for pt in geom.toList():
            v.extend(pt)
        return {"pts": v}


class SphereType(PointBasicTypeBase):

    name = "Sphere"
    pids = [PID.C, PID.OP, PID.G0]

    def setupWidgets(self, ppage):
        ppage.setupWidgets(geomItems=[{"name": "Radius", "defVal": self.defaultValue()}])

    def geometry(self, feat, geom):
        return {"pts": geom.toList(),
                "r": feat.prop(PID.G0)}


class CylinderType(PointBasicTypeBase):

    name = "Cylinder"
    pids = [PID.C, PID.OP, PID.G0, PID.G1]

    def setupWidgets(self, ppage):
        ppage.setupWidgets(geomItems=[{"name": "Radius", "defVal": self.defaultValue()},
                                      {"name": "Height", "defVal": self.defaultValueZ()}])

    def geometry(self, feat, geom):
        r = feat.prop(PID.G0)
        return {"pts": geom.toList(),
                "r": r,
                "h": feat.prop(PID.G1) * self.settings.mapTo3d().zScale}


class ConeType(CylinderType):

    name = "Cone"


class BoxType(PointBasicTypeBase):

    name = "Box"
    pids = [PID.C, PID.OP, PID.G0, PID.G1, PID.G2]

    def setupWidgets(self, ppage):
        val = self.defaultValue()

        ppage.setupWidgets(geomItems=[{"name": "Width", "defVal": val},
                                      {"name": "Depth", "defVal": val},
                                      {"name": "Height", "defVal": self.defaultValueZ()}])

    def geometry(self, feat, geom):
        return {"pts": geom.toList(),
                "w": feat.prop(PID.G0),
                "d": feat.prop(PID.G1),
                "h": feat.prop(PID.G2) * self.settings.mapTo3d().zScale}


class DiskType(PointTypeBase):

    name = "Disk"
    pids = [PID.C, PID.OP, PID.G0, PID.G1, PID.G2]

    def setupWidgets(self, ppage):
        ppage.setupWidgets(geomItems=[{"name": "Radius", "defVal": self.defaultValue()},
                                      {"name": "Dip", "label": "Degrees", "valType": WVT.ANGLE, "defVal": 0, "label_field": None},
                                      {"name": "Dip direction", "label": "Degrees", "valType": WVT.ANGLE, "defVal": 0, "label_field": None}])

    def material(self, feat):
        return {"idx": self.mtlManager.getMeshMaterialIndex(feat.prop(PID.C), feat.prop(PID.OP), doubleSide=True)}

    def geometry(self, feat, geom):
        return {"pts": geom.toList(),
                "r": feat.prop(PID.G0),
                "d": feat.prop(PID.G1),
                "dd": feat.prop(PID.G2)}


class PlaneType(PointTypeBase):

    name = "Plane"
    pids = [PID.C, PID.OP, PID.G0, PID.G1, PID.G2, PID.G3]

    def setupWidgets(self, ppage):
        val = self.defaultValue()
        ppage.setupWidgets(geomItems=[{"name": "Width", "defVal": val},
                                      {"name": "Length", "defVal": val},
                                      {"name": "Dip", "label": "Degrees", "valType": WVT.ANGLE, "defVal": 0, "label_field": None},
                                      {"name": "Dip direction", "label": "Degrees", "valType": WVT.ANGLE, "defVal": 0, "label_field": None}])

    def material(self, feat):
        return {"idx": self.mtlManager.getMeshMaterialIndex(feat.prop(PID.C), feat.prop(PID.OP), doubleSide=True)}

    def geometry(self, feat, geom):
        return {"pts": geom.toList(),
                "w": feat.prop(PID.G0),
                "l": feat.prop(PID.G1),
                "d": feat.prop(PID.G2),
                "dd": feat.prop(PID.G3)}


# Line
class LineType(LineTypeBase):

    name = "Line"
    pids = [PID.C, PID.OP, PID.M0]

    def setupWidgets(self, ppage):
        ppage.setupWidgets(mtlItems=[{"name": "Dashed", "type": PropertyWidget.CHECKBOX}])

    def material(self, feat):
        return {"idx": self.mtlManager.getLineIndex(feat.prop(PID.C), feat.prop(PID.OP), feat.prop(PID.M0))}

    def geometry(self, feat, geom):
        return {"lines": geom.toList(flat=True)}


class ThickLineType(LineTypeBase):

    name = "Thick Line"
    pids = [PID.C, PID.OP, PID.M0, PID.M1]

    def setupWidgets(self, ppage):
        ppage.setupWidgets(mtlItems=[{"name": "Thickness", "defVal": 1},
                                     {"name": "Dashed", "type": PropertyWidget.CHECKBOX}])

    def material(self, feat):
        return {"idx": self.mtlManager.getMeshLineIndex(feat.prop(PID.C), feat.prop(PID.OP), feat.prop(PID.M0), feat.prop(PID.M1))}

    def geometry(self, feat, geom):
        return {"lines": geom.toList(flat=True)}


class PipeType(LineTypeBase):

    name = "Pipe"
    pids = [PID.C, PID.OP, PID.G0]

    def setupWidgets(self, ppage):
        ppage.setupWidgets(geomItems=[{"name": "Radius", "defVal": self.defaultValue()}])

    def material(self, feat):
        return {"idx": self.mtlManager.getMeshMaterialIndex(feat.prop(PID.C), feat.prop(PID.OP))}

    def geometry(self, feat, geom):
        r = feat.prop(PID.G0)
        return {"lines": geom.toList(),
                "r": r}


class ConeLineType(PipeType):

    name = "Cone"


class BoxLineType(LineTypeBase):

    name = "Box"
    pids = [PID.C, PID.OP, PID.G0, PID.G1]

    def setupWidgets(self, ppage):
        val = self.defaultValue()
        ppage.setupWidgets(geomItems=[{"name": "Width", "defVal": val},
                                      {"name": "Height", "defVal": val}])

    def material(self, feat):
        return {"idx": self.mtlManager.getMeshMaterialIndex(feat.prop(PID.C), feat.prop(PID.OP))}

    def geometry(self, feat, geom):
        return {"lines": geom.toList(),
                "w": feat.prop(PID.G0),
                "h": feat.prop(PID.G1)}


class WallType(LineTypeBase):

    name = "Wall"
    pids = [PID.C, PID.OP, PID.ALT2]

    def setupWidgets(self, ppage):
        ppage.setupWidgets(alt2=True)

    def material(self, feat):
        return {"idx": self.mtlManager.getMeshFlatMaterialIndex(feat.prop(PID.C), feat.prop(PID.OP), doubleSide=True)}

    def geometry(self, feat, geom):
        return {"lines": geom.toList(flat=True),
                "bh": feat.prop(PID.ALT2) * self.settings.mapTo3d().zScale}


# Polygon
class PolygonType(PolygonTypeBase):

    """3d polygon support: yes"""

    name = "Polygon"
    pids = [PID.C, PID.OP]

    def setupWidgets(self, ppage):
        ppage.setupWidgets()

    def material(self, feat):
        return {"idx": self.mtlManager.getMeshFlatMaterialIndex(feat.prop(PID.C), feat.prop(PID.OP), True)}

    def geometry(self, feat, geom):
        g = geom.toDict(flat=True)
        return g


class ExtrudedType(PolygonTypeBase):

    """3d polygon support: no"""

    name = "Extruded"
    pids = [PID.C, PID.C2, PID.OP, PID.G0]

    def setupWidgets(self, ppage):
        ppage.setupWidgets(geomItems=[{"name": "Height", "defVal": self.defaultValueZ()}],
                           color2={"name": "Edge color",
                                   "itemText": {None: "No edge"},
                                   "defVal": None})

    def material(self, feat):
        mtl = {"idx": self.mtlManager.getMeshMaterialIndex(feat.prop(PID.C), feat.prop(PID.OP))}

        # edges
        if feat.prop(PID.C2) is not None:
            mtl["edge"] = self.mtlManager.getLineIndex(feat.prop(PID.C2), feat.prop(PID.OP))
        return mtl

    def geometry(self, feat, geom):
        return {
            "polygons": geom.toList2(),
            "centroids": geom.centroids,
            "h": feat.prop(PID.G0) * self.settings.mapTo3d().zScale
        }


class OverlayType(PolygonTypeBase):

    """3d polygon support: no"""

    name = "Overlay"
    pids = [PID.C, PID.C2, PID.OP]

    def setupWidgets(self, ppage):
        ppage.setupWidgets(color2={"name": "Border color",
                                   "itemText": {None: "No border"},
                                   "defVal": None})

    def material(self, feat):
        mtl = {"idx": self.mtlManager.getMeshMaterialIndex(feat.prop(PID.C), feat.prop(PID.OP), True)}

        # border
        if feat.prop(PID.C2) is not None:
            mtl["brdr"] = self.mtlManager.getLineIndex(feat.prop(PID.C2), feat.prop(PID.OP))
        return mtl

    def geometry(self, feat, geom):
        g = geom.toDict(flat=True)  # TINGeometry

        # border
        if feat.prop(PID.C2) is not None:
            g["brdr"] = [bnds.toList(flat=True) for bnds in geom.bnds_list]

        return g


# BillboardType
class BillboardType(PointTypeBase):

    name = "Billboard"
    pids = [PID.PATH, PID.OP, PID.G0]

    def setupWidgets(self, ppage):
        filterString = "Images (*.png *.jpg *.gif *.bmp);;All files (*.*)"

        ppage.setupWidgets(filepath={"name": "Image file", "filterString": filterString, "allowURL": True},
                           geomItems=[{"name": "Size", "valType": WVT.OTHERS, "defVal": 1}],
                           color=False)

    def material(self, feat):
        if feat.prop(PID.PATH):
            return {"idx": self.mtlManager.getSpriteImageIndex(feat.prop(PID.PATH), feat.prop(PID.OP))}
        return None

    def geometry(self, feat, geom):
        return {"pts": geom.toList(),
                "size": feat.prop(PID.G0)}


# ModelFileType
class ModelFileType(PointTypeBase):

    name = "3D Model"
    pids = [PID.PATH, PID.G0, PID.G1, PID.G2, PID.G3, PID.G4]
    experimental = True

    def __init__(self, settings, modelManager=None):
        PointTypeBase.__init__(self, settings)
        self.modelManager = modelManager

    def setupWidgets(self, ppage):
        filterString = "Model files (*.dae *.gltf *.glb);;All files (*.*)"

        ppage.setupWidgets(filepath={"name": "Model file", "filterString": filterString, "allowURL": True},
                           geomItems=[{"name": "Scale", "defVal": 1},
                                      {"name": "Rotation (x)", "label": "Degrees", "valType": WVT.ANGLE, "defVal": 0},
                                      {"name": "Rotation (y)", "label": "Degrees", "valType": WVT.ANGLE, "defVal": 0},
                                      {"name": "Rotation (z)", "label": "Degrees", "valType": WVT.ANGLE, "defVal": 0},
                                      {"name": "Rotation order", "type": PropertyWidget.COMBOBOX,
                                       "defVal": "XYZ", "items": ["XYZ", "XZY", "YXZ", "YZX", "ZXY", "ZYX"]}],
                           color=False,
                           opacity=False)

    def model(self, feat):
        if feat.prop(PID.PATH):
            return self.modelManager.modelIndex(feat.prop(PID.PATH))
        return None

    def geometry(self, feat, geom):
        d = {"pts": geom.toList(),
             "rotateX": feat.prop(PID.G1),
             "rotateY": feat.prop(PID.G2),
             "rotateZ": feat.prop(PID.G3),
             "scale": feat.prop(PID.G0)}

        if feat.prop(PID.G4) != "XYZ":    # added in 2.4
            d["rotateO"] = feat.prop(PID.G4)
        return d




class GeorefImageType(PolygonTypeBase):

    name = "Georeferenced Image"
    pids = [PID.PATH, PID.OP, PID.C]  # Added color for fallback
    experimental = True

    def setupWidgets(self, ppage):
        # This type is meant to be used programmatically via the georeferencer dialog
        filterString = "Images (*.png *.jpg *.gif *.bmp);;All files (*.*)"
        ppage.setupWidgets(filepath={"name": "Image file", "filterString": filterString, "allowURL": True},
                          color=True)  # Enable color as fallback

    def material(self, feat):
        from .utils import logMessage
        print("DEBUG: GeorefImageType.material() called")
        logMessage("GeorefImageType.material() called", warning=True)
        
        # Use a semi-transparent red color for testing the polygon geometry
        # This will confirm if the polygon itself is being created correctly
        return {"idx": self.mtlManager.getMeshBasicMaterialIndex("0xff0000", 0.5, True)}  # Semi-transparent red

    def geometry(self, feat, geom):
        # Debug logging
        from .utils import logMessage
        from .geometry import TINGeometry
        
        # Use direct print for easier debugging
        print("DEBUG: GeorefImageType.geometry() called")
        logMessage("GeorefImageType.geometry() - Adding UV coordinates for texture mapping", warning=True)
        
        # Create a TIN geometry object for proper formatting
        tin = TINGeometry()
        
        # Get corners from layer properties if available
        try:
            # Search through all layers for our custom properties
            for layer_id, layer in self.settings.layers.items():
                print(f"DEBUG: Checking layer {layer_id} for custom properties")
                custom_props = layer.properties.custom if hasattr(layer.properties, "custom") else None
                if custom_props and "imageCorners" in custom_props:
                    corners = custom_props["imageCorners"]
                    print(f"DEBUG: Found corners in layer {layer_id}: {corners}")
                    logMessage(f"Found corners in layer {layer_id}: {corners}", warning=True)
                    
                    # Add the triangles to our TIN geometry
                    # First triangle (corners 0, 1, 2)
                    tin.triangles.append([
                        corners[0],  # Top-left
                        corners[1],  # Top-right
                        corners[2]   # Bottom-right
                    ])
                    
                    # Second triangle (corners 0, 2, 3)
                    tin.triangles.append([
                        corners[0],  # Top-left
                        corners[2],  # Bottom-right
                        corners[3]   # Bottom-left
                    ])
                    
                    # Convert to dictionary format
                    d = tin.toDict(flat=True)
                    print(f"DEBUG: TIN dictionary created: {d}")
                    
                    # Add UV coordinates for texture mapping
                    # Format: vertices=[v1x,v1y,v1z, v2x,v2y,v2z, ...], 
                    #         uv=[[u1,v1], [u2,v2], ...]
                    d["uvs"] = [
                        # Coordinates match triangle vertices in the same order
                        [0, 0],  # Top-left (0)
                        [1, 0],  # Top-right (1)
                        [1, 1],  # Bottom-right (2)
                        [0, 1]   # Bottom-left (3)
                    ]
                    
                    # Try alternative styles of specifying texture coordinates
                    d["uv"] = d["uvs"]  # Some renderers may expect "uv" instead of "uvs"
                    
                    # Add texture flag to indicate this needs a texture
                    d["textured"] = True
                    d["uvsNeedUpdate"] = True
                    
                    # Add image path directly to geometry in case that's needed
                    d["image_path"] = feat.prop(PID.PATH)
                    
                    print(f"DEBUG: Final geometry with UVs: {d}")
                    logMessage(f"Created geometry with UVs for texture mapping", warning=True)
                    return d
        except Exception as e:
            logMessage(f"Error in geometry: {str(e)}", warning=True)
        
        # Fallback to simple implementation if no corners found
        print("DEBUG: Using fallback geometry (no corners found)")
        logMessage("Using fallback geometry (no corners found)", warning=True)
        
        # Create a simple quad centered at the point location
        center = geom.toList()[0]
        print(f"DEBUG: Center point: {center}")
        size = self.defaultValue()
        half_size = size / 2
        
        # Create simple vertices for a horizontal square
        pt1 = [center[0] - half_size, center[1] - half_size, center[2]]  # Bottom-left
        pt2 = [center[0] + half_size, center[1] - half_size, center[2]]  # Bottom-right
        pt3 = [center[0] + half_size, center[1] + half_size, center[2]]  # Top-right
        pt4 = [center[0] - half_size, center[1] + half_size, center[2]]  # Top-left
        
        # Add triangles to the TIN
        tin.triangles.append([pt4, pt3, pt2])  # First triangle
        tin.triangles.append([pt4, pt2, pt1])  # Second triangle
        
        # Convert to dictionary format
        d = tin.toDict(flat=True)
        print(f"DEBUG: Fallback TIN dictionary: {d}")
        
        # Add UV coordinates for texture mapping
        d["uvs"] = [
            [0, 0],  # Top-left (4)
            [1, 0],  # Top-right (3)
            [1, 1],  # Bottom-right (2)
            [0, 1]   # Bottom-left (1)
        ]
        
        # Try alternative styles of specifying texture coordinates
        d["uv"] = d["uvs"]  # Some renderers may expect "uv" instead of "uvs"
        
        # Add texture flag to indicate this needs a texture
        d["textured"] = True
        d["uvsNeedUpdate"] = True
        
        # Add image path directly to geometry in case that's needed
        d["image_path"] = feat.prop(PID.PATH)
        
        print(f"DEBUG: Final fallback geometry: {d}")
        logMessage(f"Created fallback geometry with UVs for texture mapping", warning=True)
        return d


class ObjectType:

    # point
    Sphere = SphereType
    Cylinder = CylinderType
    Cone = ConeType
    Box = BoxType
    Disk = DiskType
    Plane = PlaneType
    Point = PointType
    Billboard = BillboardType
    GeorefImage = GeorefImageType
    ModelFile = ModelFileType

    # line
    Line = LineType
    ThickLine = ThickLineType
    Pipe = PipeType
    ConeLine = ConeLineType
    BoxLine = BoxLineType
    Wall = WallType

    # polygon
    Polygon = PolygonType
    Extruded = ExtrudedType
    Overlay = OverlayType

    Grouped = {LayerType.POINT: [SphereType, CylinderType, ConeType, BoxType, DiskType,
                                 PlaneType, PointType, BillboardType, 
                                 GeorefImage, ModelFileType],
               LayerType.LINESTRING: [LineType, ThickLineType, PipeType, ConeLineType, BoxLineType, WallType],
               LayerType.POLYGON: [PolygonType, ExtrudedType, OverlayType]
               }

    @classmethod
    def typesByGeomType(cls, geom_type):
        return cls.Grouped.get(geom_type, [])

    @classmethod
    def typeByName(cls, name, geom_type):
        for obj_type in cls.typesByGeomType(geom_type):
            if obj_type.name == name:
                return obj_type
        return None


def tr(source):
    return source


# def _():
#     tr("Point")
