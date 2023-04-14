"""
Data Embedder Model adding visualisations to github.com/ABI-Software/dataembedder
"""
import os
import json

from cmlibs.utils.zinc.finiteelement import evaluate_field_nodeset_range
from cmlibs.utils.zinc.general import ChangeManager
from cmlibs.zinc.field import Field, FieldGroup
from cmlibs.zinc.glyph import Glyph
from cmlibs.zinc.graphics import Graphics
from cmlibs.zinc.material import Material
from dataembedder.dataembedder import DataEmbedder
from mapclientplugins.dataembedderstep.utils.zinc_utils import get_scene_selection_group, create_scene_selection_group,\
    group_add_group_elements, group_add_group_nodes


nodeDerivativeLabels = ["D1", "D2", "D3", "D12", "D13", "D23", "D123"]


class DataEmbedderModel(object):
    """
    Class adding visualisations to DataEmbedder back-end.
    """

    def __init__(self, zincScaffoldFileName: str, zincFittedGeometryFileName, zincDataFileName: str,
                 location, identifier):
        """
        :param location: Path to folder for mapclient step name.
        """
        self._dataEmbedder = DataEmbedder(zincScaffoldFileName, zincFittedGeometryFileName, zincDataFileName)
        self._location = os.path.join(location, identifier)
        self._identifier = identifier
        self._initGraphicsModules()
        self._settings = {
            "displayAxes": True,
            "displayDataMarkerPoints": True,
            "displayDataMarkerNames": False,
            "displayDataNodePoints": False,
            "displayDataLines": True,
            "displayDataEmbedded": False,
            "displayModelCoordinatesField": None,
            "displayMarkerPoints": True,
            "displayMarkerNames": False,
            "displayNodePoints": False,
            "displayNodeNumbers": False,
            "displayElementNumbers": False,
            "displayElementAxes": False,
            "displayLines": True,
            "displayLinesExterior": False,
            "displaySurfaces": True,
            "displaySurfacesExterior": True,
            "displaySurfacesTranslucent": True,
            "displaySurfacesWireframe": False
        }
        self._loadSettings()
        self._dataEmbedder.load()
        self._displayModelCoordinatesField = None
        if self._settings["displayModelCoordinatesField"]:
            displayModelCoordinatesField = self.getHostRegion().getFieldmodule().findFieldByName(
                self._settings["displayModelCoordinatesField"])
            if displayModelCoordinatesField.isValid():
                self._displayModelCoordinatesField = displayModelCoordinatesField
        if not self._displayModelCoordinatesField:
            self._displayModelCoordinatesField = self._dataEmbedder.getFittedCoordinatesField()
            self._settings["displayModelCoordinatesField"] = self._displayModelCoordinatesField.getName()

    def _initGraphicsModules(self):
        context = self._dataEmbedder.getContext()
        self._materialmodule = context.getMaterialmodule()
        with ChangeManager(self._materialmodule):
            self._materialmodule.defineStandardMaterials()
            solid_blue = self._materialmodule.createMaterial()
            solid_blue.setName("solid_blue")
            solid_blue.setManaged(True)
            solid_blue.setAttributeReal3(Material.ATTRIBUTE_AMBIENT, [0.0, 0.2, 0.6])
            solid_blue.setAttributeReal3(Material.ATTRIBUTE_DIFFUSE, [0.0, 0.7, 1.0])
            solid_blue.setAttributeReal3(Material.ATTRIBUTE_EMISSION, [0.0, 0.0, 0.0])
            solid_blue.setAttributeReal3(Material.ATTRIBUTE_SPECULAR, [0.1, 0.1, 0.1])
            solid_blue.setAttributeReal(Material.ATTRIBUTE_SHININESS, 0.2)
            trans_blue = self._materialmodule.createMaterial()
            trans_blue.setName("trans_blue")
            trans_blue.setManaged(True)
            trans_blue.setAttributeReal3(Material.ATTRIBUTE_AMBIENT, [0.0, 0.2, 0.6])
            trans_blue.setAttributeReal3(Material.ATTRIBUTE_DIFFUSE, [0.0, 0.7, 1.0])
            trans_blue.setAttributeReal3(Material.ATTRIBUTE_EMISSION, [0.0, 0.0, 0.0])
            trans_blue.setAttributeReal3(Material.ATTRIBUTE_SPECULAR, [0.1, 0.1, 0.1])
            trans_blue.setAttributeReal(Material.ATTRIBUTE_ALPHA, 0.3)
            trans_blue.setAttributeReal(Material.ATTRIBUTE_SHININESS, 0.2)
        glyphmodule = context.getGlyphmodule()
        glyphmodule.defineStandardGlyphs()
        tessellationmodule = context.getTessellationmodule()
        defaultTessellation = tessellationmodule.getDefaultTessellation()
        defaultTessellation.setRefinementFactors([12])

    def _getEmbedderSettingsFileName(self):
        return self._location + "-settings.json"

    def _getDisplaySettingsFileName(self):
        return self._location + "-display-settings.json"

    def _loadSettings(self):
        embedderSettingsFileName = self._getEmbedderSettingsFileName()
        if os.path.isfile(embedderSettingsFileName):
            with open(embedderSettingsFileName, "r") as f:
                self._dataEmbedder.decodeSettingsJSON(f.read())
        displaySettingsFileName = self._getDisplaySettingsFileName()
        if os.path.isfile(displaySettingsFileName):
            with open(displaySettingsFileName, "r") as f:
                savedSettings = json.loads(f.read())
                self._settings.update(savedSettings)

    def _saveSettings(self):
        with open(self._getEmbedderSettingsFileName(), "w") as f:
            f.write(self._dataEmbedder.encodeSettingsJSON())
        with open(self._getDisplaySettingsFileName(), "w") as f:
            f.write(json.dumps(self._settings, sort_keys=False, indent=4))

    def getFittedCoordinatesField(self) -> Field:
        return self._dataEmbedder.getFittedCoordinatesField()

    def setFittedCoordinatesField(self, field):
        if self._dataEmbedder.setFittedCoordinatesField(field):
            self.createGraphics()

    def getMaterialCoordinatesField(self) -> Field:
        return self._dataEmbedder.getMaterialCoordinatesField()

    def setMaterialCoordinatesField(self, field):
        if self._dataEmbedder.setMaterialCoordinatesField(field):
            self.createGraphics()

    def getHostMarkerGroup(self) -> Field:
        return self._dataEmbedder.getHostMarkerGroup()

    def setHostMarkerGroup(self, group):
        if self._dataEmbedder.setHostMarkerGroup(group):
            self.createGraphics()

    def getHostProjectionGroup(self) -> Field:
        return self._dataEmbedder.getHostProjectionGroup()

    def setHostProjectionGroup(self, group):
        if self._dataEmbedder.setHostProjectionGroup(group):
            self.createGraphics()

    def getDataCoordinatesField(self) -> Field:
        return self._dataEmbedder.getDataCoordinatesField()

    def setDataCoordinatesField(self, field):
        if self._dataEmbedder.setDataCoordinatesField(field):
            self.createGraphics()

    def getDataMarkerGroup(self) -> Field:
        return self._dataEmbedder.getHostMarkerGroup()

    def setDataMarkerGroup(self, group):
        if self._dataEmbedder.setDataMarkerGroup(group):
            self.createGraphics()

    def getDisplayModelCoordinatesField(self) -> Field:
        """
        Get the field to show host scaffold and embedded points on.
        :return: Zinc Field.
        """
        return self._displayModelCoordinatesField

    def setDisplayModelCoordinatesField(self, displayModelCoordinatesField: Field):
        """
        Get the field to show host scaffold and embedded points on.
        :return: Zinc Field.
        """
        assert displayModelCoordinatesField.isValid()
        if not (displayModelCoordinatesField == self._displayModelCoordinatesField):
            self._displayModelCoordinatesField = displayModelCoordinatesField
            self._settings["displayModelCoordinatesField"] = self._displayModelCoordinatesField.getName()
            self.createGraphics()

    def getOutputModelFileNameStem(self):
        return self._location

    def getOutputModelFileName(self):
        return self._location + ".exf"

    def done(self):
        self._saveSettings()
        outputRegion = self._dataEmbedder.generateOutput()
        assert outputRegion.isValid(), "DataEmbedder failed to generate output"
        outputRegion.writeFile(self.getOutputModelFileName())

    def getIdentifier(self):
        return self._identifier

    def getContext(self):
        return self._dataEmbedder.getContext()

    def getDataEmbedder(self):
        return self._dataEmbedder

    def getHostRegion(self):
        return self._dataEmbedder.getHostRegion()

    def getHostScene(self):
        return self._dataEmbedder.getHostRegion().getScene()

    def getDataRegion(self):
        return self._dataEmbedder.getDataRegion()

    def getDataScene(self):
        return self._dataEmbedder.getDataRegion().getScene()

    def getOutputDataRegion(self):
        return self._dataEmbedder.generateOutput()

    def getOutputDataScene(self):
        return self.getOutputDataRegion().getScene()

    def isDataGroupEmbed(self, groupName: str) -> bool:
        return self._dataEmbedder.isDataGroupEmbed(groupName)

    def setDataGroupEmbed(self, groupName: str, embed: bool):
        """
        Must set via this method, not through DataEmbedder directly to ensure
        data is re-embedded and graphics are updated.
        :param groupName: Name of data group to modify settings for.
        :param embed: True to embed, False to not embed.
        :return: True if embed state changed, otherwise False.
        """
        if self._dataEmbedder.setDataGroupEmbed(groupName, embed):
            self.createGraphics()
            return True
        return False

    def _getVisibility(self, graphicsName):
        return self._settings[graphicsName]

    def _setHostVisibility(self, graphicsName, show):
        self._settings[graphicsName] = show
        graphics = self.getHostScene().findGraphicsByName(graphicsName)
        graphics.setVisibilityFlag(show)

    def _setOutputDataVisibility(self, graphicsName, show):
        self._settings[graphicsName] = show
        graphics = self.getOutputDataScene().findGraphicsByName(graphicsName)
        graphics.setVisibilityFlag(show)

    def isDisplayAxes(self):
        return self._getVisibility("displayAxes")

    def setDisplayAxes(self, show):
        self._setHostVisibility("displayAxes", show)

    def isDisplayDataLines(self):
        return self._getVisibility("displayDataLines")

    def setDisplayDataLines(self, show):
        self._setOutputDataVisibility("displayDataLines", show)

    def isDisplayDataEmbedded(self):
        return self._settings["displayDataEmbedded"]

    def setDisplayDataEmbedded(self, displayDataEmbedded: bool):
        if displayDataEmbedded != self.isDisplayDataEmbedded():
            self._settings["displayDataEmbedded"] = displayDataEmbedded
            self.createGraphics()

    def isDisplayDataMarkerPoints(self):
        return self._getVisibility("displayDataMarkerPoints")

    def setDisplayDataMarkerPoints(self, show):
        self._setOutputDataVisibility("displayDataMarkerPoints", show)

    def isDisplayDataMarkerNames(self):
        return self._getVisibility("displayDataMarkerNames")

    def setDisplayDataMarkerNames(self, show):
        self._setOutputDataVisibility("displayDataMarkerNames", show)

    def isDisplayDataNodePoints(self):
        return self._getVisibility("displayDataNodePoints")

    def setDisplayDataNodePoints(self, show):
        self._setOutputDataVisibility("displayDataNodePoints", show)

    def isDisplayElementNumbers(self):
        return self._getVisibility("displayElementNumbers")

    def setDisplayElementNumbers(self, show):
        self._setHostVisibility("displayElementNumbers", show)

    def isDisplayLines(self):
        return self._getVisibility("displayLines")

    def setDisplayLines(self, show):
        self._setHostVisibility("displayLines", show)

    def isDisplayLinesExterior(self):
        return self._settings["displayLinesExterior"]

    def setDisplayLinesExterior(self, isExterior):
        self._settings["displayLinesExterior"] = isExterior
        lines = self.getHostScene().findGraphicsByName("displayLines")
        lines.setExterior(self.isDisplayLinesExterior())

    def isDisplayMarkerPoints(self):
        return self._getVisibility("displayMarkerPoints")

    def setDisplayMarkerPoints(self, show):
        self._setHostVisibility("displayMarkerPoints", show)

    def isDisplayMarkerNames(self):
        return self._getVisibility("displayMarkerNames")

    def setDisplayMarkerNames(self, show):
        self._setHostVisibility("displayMarkerNames", show)

    def isDisplayNodeNumbers(self):
        return self._getVisibility("displayNodeNumbers")

    def setDisplayNodeNumbers(self, show):
        self._setHostVisibility("displayNodeNumbers", show)

    def isDisplayNodePoints(self):
        return self._getVisibility("displayNodePoints")

    def setDisplayNodePoints(self, show):
        self._setHostVisibility("displayNodePoints", show)

    def isDisplaySurfaces(self):
        return self._getVisibility("displaySurfaces")

    def setDisplaySurfaces(self, show):
        self._setHostVisibility("displaySurfaces", show)

    def isDisplaySurfacesExterior(self):
        return self._settings["displaySurfacesExterior"]

    def setDisplaySurfacesExterior(self, isExterior):
        self._settings["displaySurfacesExterior"] = isExterior
        surfaces = self.getHostScene().findGraphicsByName("displaySurfaces")
        surfaces.setExterior(self.isDisplaySurfacesExterior()
                             if (self._dataEmbedder.getHostMesh().getDimension() == 3) else False)

    def isDisplaySurfacesTranslucent(self):
        return self._settings["displaySurfacesTranslucent"]

    def setDisplaySurfacesTranslucent(self, isTranslucent):
        self._settings["displaySurfacesTranslucent"] = isTranslucent
        surfaces = self.getHostScene().findGraphicsByName("displaySurfaces")
        surfacesMaterial = self._materialmodule.findMaterialByName("trans_blue" if isTranslucent else "solid_blue")
        surfaces.setMaterial(surfacesMaterial)

    def isDisplaySurfacesWireframe(self):
        return self._settings["displaySurfacesWireframe"]

    def setDisplaySurfacesWireframe(self, isWireframe):
        self._settings["displaySurfacesWireframe"] = isWireframe
        surfaces = self.getHostScene().findGraphicsByName("displaySurfaces")
        surfaces.setRenderPolygonMode(Graphics.RENDER_POLYGON_MODE_WIREFRAME
                                      if isWireframe else Graphics.RENDER_POLYGON_MODE_SHADED)

    def isDisplayElementAxes(self):
        return self._getVisibility("displayElementAxes")

    def setDisplayElementAxes(self, show):
        self._setHostVisibility("displayElementAxes", show)

    def needPerturbLines(self):
        """
        Return if solid surfaces are drawn with lines, requiring perturb lines to be activated.
        """
        region = self.getHostRegion()
        if region is None:
            return False
        mesh2d = region.getFieldmodule().findMeshByDimension(2)
        if mesh2d.getSize() == 0:
            return False
        return self.isDisplayLines() and self.isDisplaySurfaces() and not self.isDisplaySurfacesTranslucent()

    def clearOutputDataSelection(self):
        """
        Clear selection in the output data group.
        """
        region = self._dataEmbedder.generateOutput()
        fieldmodule = region.getFieldmodule()
        with ChangeManager(fieldmodule):
            scene = region.getScene()
            selectionGroup = scene.getSelectionField().castGroup()
            if selectionGroup.isValid():
                selectionGroup.clear()
                del selectionGroup
                scene.setSelectionField(Field())

    def setSelectHighlightOutputDataGroup(self, group: FieldGroup):
        """
        Select and highlight objects in the output data group.
        :param group: FieldGroup to select, or None to clear selection.
        """
        region = self._dataEmbedder.generateOutput()
        fieldmodule = region.getFieldmodule()
        with ChangeManager(fieldmodule):
            scene = region.getScene()
            # can't use SUBELEMENT_HANDLING_MODE_FULL as some groups have been tweaked to omit some faces
            selectionGroup = get_scene_selection_group(
                scene, subelement_handling_mode=FieldGroup.SUBELEMENT_HANDLING_MODE_NONE)
            if group:
                if selectionGroup:
                    selectionGroup.clear()
                else:
                    selectionGroup = create_scene_selection_group(
                        scene, subelement_handling_mode=FieldGroup.SUBELEMENT_HANDLING_MODE_NONE)
                group_add_group_elements(selectionGroup, group, highest_dimension_only=False)
                for fieldDomainType in (Field.DOMAIN_TYPE_NODES, Field.DOMAIN_TYPE_DATAPOINTS):
                    group_add_group_nodes(selectionGroup, group,
                                          fieldmodule.findNodesetByFieldDomainType(fieldDomainType))
            else:
                if selectionGroup:
                    selectionGroup.clear()
                    scene.setSelectionField(Field())

    def setSelectHighlightOutputDataGroupByName(self, groupName):
        """
        Select and highlight objects in the output data group by name.
        :param groupName: Name of group to select, or None to clear selection.
        """
        region = self._dataEmbedder.generateOutput()
        fieldmodule = region.getFieldmodule()
        group = None
        if groupName:
            group = fieldmodule.findFieldByName(groupName).castGroup()
            if not group.isValid():
                group = None
        self.setSelectHighlightOutputDataGroup(group)

    def createGraphics(self):
        hostFieldmodule = self.getHostRegion().getFieldmodule()
        fittedGroup = None
        if self._displayModelCoordinatesField == self._dataEmbedder.getFittedCoordinatesField():
            fittedGroup = self._dataEmbedder.getFittedGroup()
        mesh = self._dataEmbedder.getHostMesh()
        meshDimension = mesh.getDimension()
        componentsCount = self._displayModelCoordinatesField.getNumberOfComponents()

        # prepare fields and calculate axis and glyph scaling
        with ChangeManager(hostFieldmodule):
            elementDerivativesField = hostFieldmodule.createFieldConcatenate([
                hostFieldmodule.createFieldDerivative(self._displayModelCoordinatesField, d + 1)
                for d in range(meshDimension)])
            cmissNumberField = hostFieldmodule.findFieldByName("cmiss_number")

            # get sizing for axes
            axesScale = 1.0
            nodes = hostFieldmodule.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
            minX, maxX = evaluate_field_nodeset_range(self._displayModelCoordinatesField, nodes)
            if componentsCount == 1:
                maxRange = maxX - minX
            else:
                maxRange = maxX[0] - minX[0]
                for c in range(1, componentsCount):
                    maxRange = max(maxRange, maxX[c] - minX[c])
            if maxRange > 0.0:
                while axesScale*10.0 < maxRange:
                    axesScale *= 10.0
                while axesScale*0.1 > maxRange:
                    axesScale *= 0.1

            # fixed width glyph size is based on average element size in all dimensions
            mesh1d = hostFieldmodule.findMeshByDimension(1)
            lineCount = mesh1d.getSize()
            if lineCount > 0:
                one = hostFieldmodule.createFieldConstant(1.0)
                sumLineLength = hostFieldmodule.createFieldMeshIntegral(one, self._displayModelCoordinatesField, mesh1d)
                cache = hostFieldmodule.createFieldcache()
                result, totalLineLength = sumLineLength.evaluateReal(cache, 1)
                glyphWidth = 0.1*totalLineLength/lineCount
                del cache
                del sumLineLength
                del one
            if (lineCount == 0) or (glyphWidth == 0.0):
                # use function of coordinate range if no elements
                if componentsCount == 1:
                    maxScale = maxX - minX
                else:
                    first = True
                    for c in range(componentsCount):
                        scale = maxX[c] - minX[c]
                        if first or (scale > maxScale):
                            maxScale = scale
                            first = False
                if maxScale == 0.0:
                    maxScale = 1.0
                glyphWidth = 0.01*maxScale
            glyphWidthMedium = 0.5*glyphWidth
            glyphWidthSmall = 0.25*glyphWidth

            hostMarkerGroup = self._dataEmbedder.getHostMarkerGroup()
            hostMarkerCoordinates = self._dataEmbedder.getHostMarkerCoordinatesField(self._displayModelCoordinatesField)
            hostMarkerNameField = self._dataEmbedder.getHostMarkerNameField()

        # make host region graphics
        scene = self.getHostScene()
        with ChangeManager(scene):
            scene.removeAllGraphics()

            axes = scene.createGraphicsPoints()
            pointattr = axes.getGraphicspointattributes()
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_AXES_XYZ)
            pointattr.setBaseSize([axesScale, axesScale, axesScale])
            pointattr.setLabelText(1, "  " + str(axesScale))
            axes.setMaterial(self._materialmodule.findMaterialByName("grey50"))
            axes.setName("displayAxes")
            axes.setVisibilityFlag(self.isDisplayAxes())

            markerPoints = scene.createGraphicsPoints()
            markerPoints.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
            if hostMarkerGroup:
                markerPoints.setSubgroupField(hostMarkerGroup)
            if hostMarkerCoordinates:
                markerPoints.setCoordinateField(hostMarkerCoordinates)
            pointattr = markerPoints.getGraphicspointattributes()
            pointattr.setBaseSize([glyphWidthSmall, glyphWidthSmall, glyphWidthSmall])
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_CROSS)
            markerPoints.setMaterial(self._materialmodule.findMaterialByName("white"))
            markerPoints.setName("displayMarkerPoints")
            markerPoints.setVisibilityFlag(self.isDisplayMarkerPoints())

            markerNames = scene.createGraphicsPoints()
            markerNames.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
            if hostMarkerGroup:
                markerNames.setSubgroupField(hostMarkerGroup)
            if hostMarkerCoordinates:
                markerNames.setCoordinateField(hostMarkerCoordinates)
            pointattr = markerNames.getGraphicspointattributes()
            pointattr.setBaseSize([glyphWidthSmall, glyphWidthSmall, glyphWidthSmall])
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_NONE)
            if hostMarkerNameField:
                pointattr.setLabelField(hostMarkerNameField)
            markerNames.setMaterial(self._materialmodule.findMaterialByName("white"))
            markerNames.setName("displayMarkerNames")
            markerNames.setVisibilityFlag(self.isDisplayMarkerNames())

            nodePoints = scene.createGraphicsPoints()
            nodePoints.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
            if fittedGroup:
                nodePoints.setSubgroupField(fittedGroup)
            nodePoints.setCoordinateField(self._displayModelCoordinatesField)
            pointattr = nodePoints.getGraphicspointattributes()
            pointattr.setBaseSize([glyphWidth, glyphWidth, glyphWidth])
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)
            nodePoints.setMaterial(self._materialmodule.findMaterialByName("white"))
            nodePoints.setName("displayNodePoints")
            nodePoints.setVisibilityFlag(self.isDisplayNodePoints())

            nodeNumbers = scene.createGraphicsPoints()
            nodeNumbers.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
            if fittedGroup:
                nodeNumbers.setSubgroupField(fittedGroup)
            nodeNumbers.setCoordinateField(self._displayModelCoordinatesField)
            pointattr = nodeNumbers.getGraphicspointattributes()
            pointattr.setLabelField(cmissNumberField)
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_NONE)
            nodeNumbers.setMaterial(self._materialmodule.findMaterialByName("green"))
            nodeNumbers.setName("displayNodeNumbers")
            nodeNumbers.setVisibilityFlag(self.isDisplayNodeNumbers())

            elementNumbers = scene.createGraphicsPoints()
            elementNumbers.setFieldDomainType(Field.DOMAIN_TYPE_MESH_HIGHEST_DIMENSION)
            if fittedGroup:
                elementNumbers.setSubgroupField(fittedGroup)
            elementNumbers.setCoordinateField(self._displayModelCoordinatesField)
            pointattr = elementNumbers.getGraphicspointattributes()
            pointattr.setLabelField(cmissNumberField)
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_NONE)
            elementNumbers.setMaterial(self._materialmodule.findMaterialByName("cyan"))
            elementNumbers.setName("displayElementNumbers")
            elementNumbers.setVisibilityFlag(self.isDisplayElementNumbers())

            elementAxes = scene.createGraphicsPoints()
            elementAxes.setFieldDomainType(Field.DOMAIN_TYPE_MESH_HIGHEST_DIMENSION)
            if fittedGroup:
                elementAxes.setSubgroupField(fittedGroup)
            elementAxes.setCoordinateField(self._displayModelCoordinatesField)
            pointattr = elementAxes.getGraphicspointattributes()
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_AXES_123)
            pointattr.setOrientationScaleField(elementDerivativesField)
            if meshDimension == 1:
                pointattr.setBaseSize([0.0, 2*glyphWidth, 2*glyphWidth])
                pointattr.setScaleFactors([0.25, 0.0, 0.0])
            elif meshDimension == 2:
                pointattr.setBaseSize([0.0, 0.0, 2*glyphWidth])
                pointattr.setScaleFactors([0.25, 0.25, 0.0])
            else:
                pointattr.setBaseSize([0.0, 0.0, 0.0])
                pointattr.setScaleFactors([0.25, 0.25, 0.25])
            elementAxes.setMaterial(self._materialmodule.findMaterialByName("yellow"))
            elementAxes.setName("displayElementAxes")
            elementAxes.setVisibilityFlag(self.isDisplayElementAxes())

            lines = scene.createGraphicsLines()
            if fittedGroup:
                lines.setSubgroupField(fittedGroup)
            lines.setCoordinateField(self._displayModelCoordinatesField)
            lines.setExterior(self.isDisplayLinesExterior())
            lines.setName("displayLines")
            lines.setVisibilityFlag(self.isDisplayLines())

            surfaces = scene.createGraphicsSurfaces()
            if fittedGroup:
                surfaces.setSubgroupField(fittedGroup)
            surfaces.setCoordinateField(self._displayModelCoordinatesField)
            surfaces.setRenderPolygonMode(Graphics.RENDER_POLYGON_MODE_WIREFRAME if self.isDisplaySurfacesWireframe()
                                          else Graphics.RENDER_POLYGON_MODE_SHADED)
            surfaces.setExterior(self.isDisplaySurfacesExterior() if (meshDimension == 3) else False)
            surfacesMaterial = self._materialmodule.findMaterialByName(
                "trans_blue" if self.isDisplaySurfacesTranslucent() else "solid_blue")
            surfaces.setMaterial(surfacesMaterial)
            surfaces.setName("displaySurfaces")
            surfaces.setVisibilityFlag(self.isDisplaySurfaces())

        outputDataRegion = self._dataEmbedder.generateOutput()
        outputDataFieldmodule = outputDataRegion.getFieldmodule()
        with ChangeManager(outputDataFieldmodule):
            # find most equivalent fields by name in outputDataRegion
            if self.isDisplayDataEmbedded():
                dataCoordinatesField =\
                    self._dataEmbedder.getOutputDataHostCoordinatesField(self._displayModelCoordinatesField)
                dataMarkerCoordinatesField = dataCoordinatesField
            else:
                dataCoordinatesField = self._dataEmbedder.getDataCoordinatesField()
                dataCoordinatesField = outputDataFieldmodule.findFieldByName(dataCoordinatesField.getName())
                dataMarkerCoordinatesField = self._dataEmbedder.getDataMarkerCoordinatesField()
                if dataMarkerCoordinatesField:
                    dataMarkerCoordinatesField =\
                        outputDataFieldmodule.findFieldByName(dataMarkerCoordinatesField.getName())
            dataMarkerGroup = self._dataEmbedder.getDataMarkerGroup()
            if dataMarkerGroup:
                dataMarkerGroup = outputDataFieldmodule.findFieldByName(dataMarkerGroup.getName())
            dataMarkerNameField = self._dataEmbedder.getDataMarkerNameField()
            if dataMarkerNameField:
                dataMarkerNameField = outputDataFieldmodule.findFieldByName(dataMarkerNameField.getName())

        # make data region graphics
        scene = outputDataRegion.getScene()
        with ChangeManager(scene):
            scene.removeAllGraphics()

            dataMarkerPoints = scene.createGraphicsPoints()
            dataMarkerPoints.setFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
            if dataMarkerGroup:
                dataMarkerPoints.setSubgroupField(dataMarkerGroup)
            if dataMarkerCoordinatesField:
                dataMarkerPoints.setCoordinateField(dataMarkerCoordinatesField)
            pointattr = dataMarkerPoints.getGraphicspointattributes()
            pointattr.setBaseSize([glyphWidthSmall, glyphWidthSmall, glyphWidthSmall])
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_CROSS)
            dataMarkerPoints.setMaterial(self._materialmodule.findMaterialByName("yellow"))
            dataMarkerPoints.setName("displayDataMarkerPoints")
            dataMarkerPoints.setVisibilityFlag(self.isDisplayDataMarkerPoints())

            dataMarkerNames = scene.createGraphicsPoints()
            dataMarkerNames.setFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
            if dataMarkerGroup:
                dataMarkerNames.setSubgroupField(dataMarkerGroup)
            if dataMarkerCoordinatesField:
                dataMarkerNames.setCoordinateField(dataMarkerCoordinatesField)
            pointattr = dataMarkerNames.getGraphicspointattributes()
            pointattr.setBaseSize([glyphWidthSmall, glyphWidthSmall, glyphWidthSmall])
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_NONE)
            if dataMarkerNameField:
                pointattr.setLabelField(dataMarkerNameField)
            dataMarkerNames.setMaterial(self._materialmodule.findMaterialByName("yellow"))
            dataMarkerNames.setName("displayDataMarkerNames")
            dataMarkerNames.setVisibilityFlag(self.isDisplayDataMarkerNames())

            dataNodePoints = scene.createGraphicsPoints()
            dataNodePoints.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
            dataNodePoints.setCoordinateField(dataCoordinatesField)
            pointattr = dataNodePoints.getGraphicspointattributes()
            pointattr.setBaseSize([glyphWidthMedium, glyphWidthMedium, glyphWidthMedium])
            pointattr.setGlyphShapeType(Glyph.SHAPE_TYPE_DIAMOND)
            dataNodePoints.setMaterial(self._materialmodule.findMaterialByName("gold"))
            dataNodePoints.setName("displayDataNodePoints")
            dataNodePoints.setVisibilityFlag(self.isDisplayDataNodePoints())

            dataLines = scene.createGraphicsLines()
            dataLines.setCoordinateField(dataCoordinatesField)
            dataLines.setName("displayDataLines")
            dataLines.setMaterial(self._materialmodule.findMaterialByName("yellow"))
            dataLines.setVisibilityFlag(self.isDisplayDataLines())
