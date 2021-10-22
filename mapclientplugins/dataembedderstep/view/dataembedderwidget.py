"""
User interface for github.com/ABI-Software/dataembedder
"""
from PySide2 import QtCore, QtGui, QtWidgets

from mapclientplugins.dataembedderstep.view.ui_dataembedderwidget import Ui_DataEmbedderWidget
from opencmiss.utils.maths.vectorops import dot, magnitude, mult, normalize, sub
from opencmiss.utils.zinc.field import field_is_managed_coordinates, field_is_managed_group


class DataEmbedderWidget(QtWidgets.QWidget):
    """
    User interface for github.com/ABI-Software/dataembedder
    """

    def __init__(self, model, parent=None):
        """
        """
        super(DataEmbedderWidget, self).__init__(parent)
        self._ui = Ui_DataEmbedderWidget()
        self._ui.setupUi(self)
        self._ui.sceneviewerwidget.setContext(model.getContext())
        self._model = model
        self._dataEmbedder = self._model.getDataEmbedder()
        self._currentGroupName = None
        self._ui.sceneviewerwidget.graphicsInitialized.connect(self._graphicsInitialized)
        self._doneCallback = None
        self._setupConfigWidgets()
        self._updateDisplayWidgets()
        self._makeConnections()
        self._buildGroupsList()

    def _graphicsInitialized(self):
        """
        Callback for when SceneviewerWidget is initialised
        """
        self._sceneChanged()
        sceneviewer = self._ui.sceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            sceneviewer.setTransparencyMode(sceneviewer.TRANSPARENCY_MODE_SLOW)
            self._autoPerturbLines()
            sceneviewer.viewAll()

    def _sceneChanged(self):
        """
        Set custom scene from model.
        """
        sceneviewer = self._ui.sceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            self._model.createGraphics()
            sceneviewer.setScene(self._model.getHostRegion().getScene())
            if self._currentGroupName:
                self._model.setSelectHighlightDataGroupByName(self._currentGroupName)

    def _makeConnections(self):
        self._makeConnectionsConfig()
        self._makeConnectionsDisplay()
        self._makeConnectionsGeneral()
        self._makeConnectionsGroup()

    def registerDoneExecution(self, callback):
        self._doneCallback = callback

    def _autoPerturbLines(self):
        """
        Enable scene viewer perturb lines iff solid surfaces are drawn with lines.
        Call whenever lines, surfaces or translucency changes
        """
        sceneviewer = self._ui.sceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            sceneviewer.setPerturbLinesFlag(self._model.needPerturbLines())

    # === config widgets ===

    def _setupConfigWidgets(self):
        """
        Set up widgets for setting initial configuration, mostly field and groups.
        """
        hostRegion = self._model.getHostRegion()
        dataRegion = self._model.getDataRegion()
        self._ui.configFittedCoordinates_fieldChooser.setRegion(hostRegion)
        self._ui.configFittedCoordinates_fieldChooser.setConditional(field_is_managed_coordinates)
        self._ui.configFittedCoordinates_fieldChooser.setField(self._model.getFittedCoordinatesField())
        self._ui.configMaterialCoordinates_fieldChooser.setRegion(hostRegion)
        self._ui.configMaterialCoordinates_fieldChooser.setConditional(field_is_managed_coordinates)
        self._ui.configMaterialCoordinates_fieldChooser.setField(self._model.getMaterialCoordinatesField())
        self._ui.configHostMarkerGroup_fieldChooser.setRegion(hostRegion)
        self._ui.configHostMarkerGroup_fieldChooser.setNullObjectName("-")
        self._ui.configHostMarkerGroup_fieldChooser.setConditional(field_is_managed_group)
        self._ui.configHostMarkerGroup_fieldChooser.setField(self._model.getHostMarkerGroup())
        self._ui.configDataCoordinates_fieldChooser.setRegion(dataRegion)
        self._ui.configDataCoordinates_fieldChooser.setConditional(field_is_managed_coordinates)
        self._ui.configDataCoordinates_fieldChooser.setField(self._model.getDataCoordinatesField())
        self._ui.configDataMarkerGroup_fieldChooser.setRegion(dataRegion)
        self._ui.configDataMarkerGroup_fieldChooser.setNullObjectName("-")
        self._ui.configDataMarkerGroup_fieldChooser.setConditional(field_is_managed_group)
        self._ui.configDataMarkerGroup_fieldChooser.setField(self._model.getDataMarkerGroup())
        self._ui.configDiagnosticLevel_spinBox.setValue(self._dataEmbedder.getDiagnosticLevel())

    def _makeConnectionsConfig(self):
        self._ui.configFittedCoordinates_fieldChooser.currentIndexChanged.connect(
            self._configFittedCoordinatesFieldChanged)
        self._ui.configMaterialCoordinates_fieldChooser.currentIndexChanged.connect(
            self._configMaterialCoordinatesFieldChanged)
        self._ui.configHostMarkerGroup_fieldChooser.currentIndexChanged.connect(self._configHostMarkerGroupChanged)
        self._ui.configDataCoordinates_fieldChooser.currentIndexChanged.connect(
            self._configDataCoordinatesFieldChanged)
        self._ui.configDataMarkerGroup_fieldChooser.currentIndexChanged.connect(self._configDataMarkerGroupChanged)
        self._ui.configDiagnosticLevel_spinBox.valueChanged.connect(self._configDiagnosticLevelValueChanged)

    def _configFittedCoordinatesFieldChanged(self, index):
        """
        Callback for change in fitted coordinates field chooser widget.
        """
        self._model.setFittedCoordinatesField(self._ui.configFittedCoordinates_fieldChooser.getField())

    def _configMaterialCoordinatesFieldChanged(self, index):
        """
        Callback for change in fitted coordinates field chooser widget.
        """
        self._model.setMaterialCoordinatesField(self._ui.configMaterialCoordinates_fieldChooser.getField())

    def _configHostMarkerGroupChanged(self, index):
        """
        Callback for change in marker group field chooser widget.
        """
        self._model.setHostMarkerGroup(self._ui.configHostMarkerGroup_fieldChooser.getField())

    def _configDataCoordinatesFieldChanged(self, index):
        """
        Callback for change in data coordinates field chooser widget.
        """
        self._model.setDataCoordinatesField(self._ui.configDataCoordinates_fieldChooser.getField())

    def _configDataMarkerGroupChanged(self, index):
        """
        Callback for change in data marker group field chooser widget.
        """
        self._model.setDataMarkerGroup(self._ui.configDataMarkerGroup_fieldChooser.getField())

    def _configDiagnosticLevelValueChanged(self, value):
        self._dataEmbedder.setDiagnosticLevel(value)

    # === display widgets ===

    def _makeConnectionsDisplay(self):
        self._ui.displayAxes_checkBox.clicked.connect(self._displayAxesClicked)
        self._ui.displayDataMarkerPoints_checkBox.clicked.connect(self._displayDataMarkerPointsClicked)
        self._ui.displayDataMarkerNames_checkBox.clicked.connect(self._displayDataMarkerNamesClicked)
        self._ui.displayMarkerPoints_checkBox.clicked.connect(self._displayMarkerPointsClicked)
        self._ui.displayMarkerNames_checkBox.clicked.connect(self._displayMarkerNamesClicked)
        self._ui.displayDataNodePoints_checkBox.clicked.connect(self._displayDataNodePointsClicked)
        self._ui.displayDataLines_checkBox.clicked.connect(self._displayDataLinesClicked)
        self._ui.displayDataEmbedded_checkBox.clicked.connect(self._displayDataEmbeddedClicked)
        self._ui.displayModelCoordinates_fieldChooser.setRegion(self._model.getHostRegion())
        self._ui.displayModelCoordinates_fieldChooser.setNullObjectName("-")
        self._ui.displayModelCoordinates_fieldChooser.setConditional(field_is_managed_coordinates)
        self._ui.displayModelCoordinates_fieldChooser.setField(self._model.getDisplayModelCoordinatesField())
        self._ui.displayModelCoordinates_fieldChooser.currentIndexChanged.connect(
            self._displayModelCoordinatesFieldChanged)
        self._ui.displayNodePoints_checkBox.clicked.connect(self._displayNodePointsClicked)
        self._ui.displayNodeNumbers_checkBox.clicked.connect(self._displayNodeNumbersClicked)
        self._ui.displayElementAxes_checkBox.clicked.connect(self._displayElementAxesClicked)
        self._ui.displayElementNumbers_checkBox.clicked.connect(self._displayElementNumbersClicked)
        self._ui.displayLines_checkBox.clicked.connect(self._displayLinesClicked)
        self._ui.displayLinesExterior_checkBox.clicked.connect(self._displayLinesExteriorClicked)
        self._ui.displaySurfaces_checkBox.clicked.connect(self._displaySurfacesClicked)
        self._ui.displaySurfacesExterior_checkBox.clicked.connect(self._displaySurfacesExteriorClicked)
        self._ui.displaySurfacesTranslucent_checkBox.clicked.connect(self._displaySurfacesTranslucentClicked)
        self._ui.displaySurfacesWireframe_checkBox.clicked.connect(self._displaySurfacesWireframeClicked)

    def _updateDisplayWidgets(self):
        """
        Update display widgets to display settings for model graphics display.
        """
        self._ui.displayAxes_checkBox.setChecked(self._model.isDisplayAxes())
        self._ui.displayDataMarkerPoints_checkBox.setChecked(self._model.isDisplayDataMarkerPoints())
        self._ui.displayDataMarkerNames_checkBox.setChecked(self._model.isDisplayDataMarkerNames())
        self._ui.displayDataNodePoints_checkBox.setChecked(self._model.isDisplayDataNodePoints())
        self._ui.displayDataLines_checkBox.setChecked(self._model.isDisplayDataLines())
        self._ui.displayDataEmbedded_checkBox.setChecked(self._model.isDisplayDataEmbedded())
        self._ui.displayModelCoordinates_fieldChooser.setField(self._model.getDisplayModelCoordinatesField())
        self._ui.displayMarkerPoints_checkBox.setChecked(self._model.isDisplayMarkerPoints())
        self._ui.displayMarkerNames_checkBox.setChecked(self._model.isDisplayMarkerNames())
        self._ui.displayNodePoints_checkBox.setChecked(self._model.isDisplayNodePoints())
        self._ui.displayNodeNumbers_checkBox.setChecked(self._model.isDisplayNodeNumbers())
        self._ui.displayElementNumbers_checkBox.setChecked(self._model.isDisplayElementNumbers())
        self._ui.displayElementAxes_checkBox.setChecked(self._model.isDisplayElementAxes())
        self._ui.displayLines_checkBox.setChecked(self._model.isDisplayLines())
        self._ui.displayLinesExterior_checkBox.setChecked(self._model.isDisplayLinesExterior())
        self._ui.displaySurfaces_checkBox.setChecked(self._model.isDisplaySurfaces())
        self._ui.displaySurfacesExterior_checkBox.setChecked(self._model.isDisplaySurfacesExterior())
        self._ui.displaySurfacesTranslucent_checkBox.setChecked(self._model.isDisplaySurfacesTranslucent())
        self._ui.displaySurfacesWireframe_checkBox.setChecked(self._model.isDisplaySurfacesWireframe())

    def _displayAxesClicked(self):
        self._model.setDisplayAxes(self._ui.displayAxes_checkBox.isChecked())

    def _displayDataMarkerPointsClicked(self):
        self._model.setDisplayDataMarkerPoints(self._ui.displayDataMarkerPoints_checkBox.isChecked())

    def _displayDataMarkerNamesClicked(self):
        self._model.setDisplayDataMarkerNames(self._ui.displayDataMarkerNames_checkBox.isChecked())

    def _displayDataNodePointsClicked(self):
        self._model.setDisplayDataNodePoints(self._ui.displayDataNodePoints_checkBox.isChecked())

    def _displayDataLinesClicked(self):
        self._model.setDisplayDataLines(self._ui.displayDataLines_checkBox.isChecked())

    def _displayDataEmbeddedClicked(self):
        self._model.setDisplayDataEmbedded(self._ui.displayDataEmbedded_checkBox.isChecked())

    def _displayModelCoordinatesFieldChanged(self, index):
        """
        Callback for change in display model coordinates field chooser widget.
        """
        field = self._ui.displayModelCoordinates_fieldChooser.getField()
        if field:
            self._model.setDisplayModelCoordinatesField(field)

    def _displayMarkerPointsClicked(self):
        self._model.setDisplayMarkerPoints(self._ui.displayMarkerPoints_checkBox.isChecked())

    def _displayMarkerNamesClicked(self):
        self._model.setDisplayMarkerNames(self._ui.displayMarkerNames_checkBox.isChecked())

    def _displayNodePointsClicked(self):
        self._model.setDisplayNodePoints(self._ui.displayNodePoints_checkBox.isChecked())

    def _displayNodeNumbersClicked(self):
        self._model.setDisplayNodeNumbers(self._ui.displayNodeNumbers_checkBox.isChecked())

    def _displayElementAxesClicked(self):
        self._model.setDisplayElementAxes(self._ui.displayElementAxes_checkBox.isChecked())

    def _displayElementNumbersClicked(self):
        self._model.setDisplayElementNumbers(self._ui.displayElementNumbers_checkBox.isChecked())

    def _displayLinesClicked(self):
        self._model.setDisplayLines(self._ui.displayLines_checkBox.isChecked())
        self._autoPerturbLines()

    def _displayLinesExteriorClicked(self):
        self._model.setDisplayLinesExterior(self._ui.displayLinesExterior_checkBox.isChecked())

    def _displaySurfacesClicked(self):
        self._model.setDisplaySurfaces(self._ui.displaySurfaces_checkBox.isChecked())
        self._autoPerturbLines()

    def _displaySurfacesExteriorClicked(self):
        self._model.setDisplaySurfacesExterior(self._ui.displaySurfacesExterior_checkBox.isChecked())

    def _displaySurfacesTranslucentClicked(self):
        self._model.setDisplaySurfacesTranslucent(self._ui.displaySurfacesTranslucent_checkBox.isChecked())
        self._autoPerturbLines()

    def _displaySurfacesWireframeClicked(self):
        self._model.setDisplaySurfacesWireframe(self._ui.displaySurfacesWireframe_checkBox.isChecked())

    # === general widgets ===

    def _makeConnectionsGeneral(self):
        self._ui.done_pushButton.clicked.connect(self._doneButtonClicked)
        self._ui.stdViews_pushButton.clicked.connect(self._stdViewsButtonClicked)
        self._ui.viewAll_pushButton.clicked.connect(self._viewAllButtonClicked)

    def _doneButtonClicked(self):
        self._model.done()
        self._ui.dockWidget.setFloating(False)
        self._doneCallback()

    def _stdViewsButtonClicked(self):
        sceneviewer = self._ui.sceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            result, eyePosition, lookAtPosition, upVector = sceneviewer.getLookatParameters()
            upVector = normalize(upVector)
            viewVector = sub(lookAtPosition, eyePosition)
            viewDistance = magnitude(viewVector)
            viewVector = normalize(viewVector)
            # viewX = dot(viewVector, [1.0, 0.0, 0.0])
            viewY = dot(viewVector, [0.0, 1.0, 0.0])
            viewZ = dot(viewVector, [0.0, 0.0, 1.0])
            # upX = dot(upVector, [1.0, 0.0, 0.0])
            upY = dot(upVector, [0.0, 1.0, 0.0])
            upZ = dot(upVector, [0.0, 0.0, 1.0])
            if (viewZ < -0.999) and (upY > 0.999):
                # XY -> XZ
                viewVector = [0.0, 1.0, 0.0]
                upVector = [0.0, 0.0, 1.0]
            elif (viewY > 0.999) and (upZ > 0.999):
                # XZ -> YZ
                viewVector = [-1.0, 0.0, 0.0]
                upVector = [0.0, 0.0, 1.0]
            else:
                # XY
                viewVector = [0.0, 0.0, -1.0]
                upVector = [0.0, 1.0, 0.0]
            eyePosition = sub(lookAtPosition, mult(viewVector, viewDistance))
            sceneviewer.setLookatParametersNonSkew(eyePosition, lookAtPosition, upVector)

    def _viewAllButtonClicked(self):
        self._ui.sceneviewerwidget.viewAll()

    # === group setting widgets ===

    def _makeConnectionsGroup(self):
        self._ui.groups_listView.clicked[QtCore.QModelIndex].connect(self._groupsListItemClicked)

    def _groupsListItemClicked(self, modelIndex):
        """
        Changes current step and possibly changes checked/run status.
        """
        model = modelIndex.model()
        item = model.itemFromIndex(modelIndex)
        groupName = item.text()
        embed = (item.checkState() == QtCore.Qt.Checked)
        self._model.setDataGroupEmbed(groupName, embed)
        if embed:
            self._model.setSelectHighlightOutputDataGroupByName(groupName)
        else:
            self._model.clearOutputDataSelection()
        if groupName != self._currentGroupName:
            self._currentGroupName = groupName
            self._updateGroupWidgets()

    def _buildGroupsList(self):
        """
        Fill the graphics list view with the list of graphics for current region/scene
        """
        self._groupsItems = QtGui.QStandardItemModel(self._ui.groups_listView)
        selectedIndex = None
        groupNames = self._dataEmbedder.getDataGroupNames()
        for groupName in groupNames:
            item = QtGui.QStandardItem(groupName)
            item.setEditable(False)
            item.setCheckable(True)
            item.setCheckState(QtCore.Qt.Checked if self._model.isDataGroupEmbed(groupName) else QtCore.Qt.Unchecked)
            self._groupsItems.appendRow(item)
            if groupName == self._currentGroupName:
                selectedIndex = self._groupsItems.indexFromItem(item)
        self._ui.groups_listView.setModel(self._groupsItems)
        if selectedIndex:
            self._ui.groups_listView.setCurrentIndex(selectedIndex)
        self._ui.groups_listView.show()
        self._updateGroupWidgets()

    def _updateGroupWidgets(self):
        """
        Update and display widgets for current group
        """
        self._ui.groupDimension_lineEdit.setText(str(self._dataEmbedder.getDataGroupDimension(self._currentGroupName)))
        self._ui.groupSize_lineEdit.setText(str(self._dataEmbedder.getDataGroupSize(self._currentGroupName)))
