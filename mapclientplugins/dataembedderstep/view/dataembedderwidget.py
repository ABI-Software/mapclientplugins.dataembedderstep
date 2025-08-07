"""
User interface for github.com/ABI-Software/dataembedder
"""
import webbrowser

from PySide6 import QtCore, QtGui, QtWidgets
from cmlibs.maths.vectorops import dot, magnitude, mult, normalize, sub
from cmlibs.widgets.collapsibleboxwidget import CollapsibleBox
from cmlibs.widgets.helpers.widgetvisibility import setting_visibility
from cmlibs.widgets.ui.ui_buttonswidget import Ui_Buttons
from cmlibs.widgets.ui.ui_displaysettingswidget import Ui_DisplaySettings
from cmlibs.utils.zinc.field import field_is_managed_coordinates, field_is_managed_group

from mapclientplugins.dataembedderstep.view.ui_dataembedderwidget import Ui_DataEmbedderWidget
from mapclientplugins.dataembedderstep.view.ui_configurationwidget import Ui_Configuration
from mapclientplugins.dataembedderstep.view.ui_datagroupswidget import Ui_DataGroups


class DataEmbedderWidget(QtWidgets.QMainWindow):
    """
    User interface for github.com/ABI-Software/dataembedder
    """

    def __init__(self, model, parent=None):
        """
        """
        super(DataEmbedderWidget, self).__init__(parent)
        self._model = model
        self._ui = Ui_DataEmbedderWidget()
        self._ui.setupUi(self)
        self._setup_dock_widget()
        self._ui.sceneviewerwidget.setContext(model.getContext())
        self._dataEmbedder = self._model.getDataEmbedder()
        self._currentGroupName = None
        self._ui.sceneviewerwidget.graphicsInitialized.connect(self._graphicsInitialized)
        self._doneCallback = None
        self._setupConfigWidgets()
        self._updateDisplayWidgets()
        self._makeConnections()
        self._buildGroupsList()

    def _setup_dock_widget(self):
        """
        Set up the dock widget for the data embedder.
        """
        parent_widget = QtWidgets.QWidget(self)

        layout = QtWidgets.QVBoxLayout(parent_widget)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)

        self._identifier_label = QtWidgets.QLabel("Identifier: " + self._model.getIdentifier())
        layout.addWidget(self._identifier_label)

        self._configuration_ui = Ui_Configuration()
        self._data_groups_ui = Ui_DataGroups()
        self._display_settings_ui = Ui_DisplaySettings()
        self._buttons_ui = Ui_Buttons()

        for ui in [self._configuration_ui, self._data_groups_ui, self._display_settings_ui]:
            form_container = QtWidgets.QWidget()
            ui.setupUi(form_container)
            tools_box = CollapsibleBox(form_container.windowTitle(), checked=True if ui is self._configuration_ui else False)
            tools_box.add_widget(form_container)
            layout.addWidget(tools_box, stretch=1)

        spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        layout.addSpacerItem(spacer)

        form_container = QtWidgets.QWidget()
        self._buttons_ui.setupUi(form_container)
        layout.addWidget(form_container)

        setting_visibility(self._display_settings_ui, 'dataembedder')

        self._dock_widget = QtWidgets.QDockWidget("Controls", self)
        self._dock_widget.setObjectName("ControlsDock")
        self._dock_widget.setWidget(parent_widget)

        self.addDockWidget(QtCore.Qt.DockWidgetArea.LeftDockWidgetArea, self._dock_widget)

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
        self._configuration_ui.configFittedCoordinates_fieldChooser.setRegion(hostRegion)
        self._configuration_ui.configFittedCoordinates_fieldChooser.setConditional(field_is_managed_coordinates)
        self._configuration_ui.configFittedCoordinates_fieldChooser.setField(self._model.getFittedCoordinatesField())
        self._configuration_ui.configMaterialCoordinates_fieldChooser.setRegion(hostRegion)
        self._configuration_ui.configMaterialCoordinates_fieldChooser.setConditional(field_is_managed_coordinates)
        self._configuration_ui.configMaterialCoordinates_fieldChooser.setField(self._model.getMaterialCoordinatesField())
        self._configuration_ui.configHostMarkerGroup_fieldChooser.setRegion(hostRegion)
        self._configuration_ui.configHostMarkerGroup_fieldChooser.setNullObjectName("-")
        self._configuration_ui.configHostMarkerGroup_fieldChooser.setConditional(field_is_managed_group)
        self._configuration_ui.configHostMarkerGroup_fieldChooser.setField(self._model.getHostMarkerGroup())
        self._configuration_ui.configHostProjectionGroup_fieldChooser.setRegion(hostRegion)
        self._configuration_ui.configHostProjectionGroup_fieldChooser.setNullObjectName("-")
        self._configuration_ui.configHostProjectionGroup_fieldChooser.setConditional(field_is_managed_group)
        self._configuration_ui.configHostProjectionGroup_fieldChooser.setField(self._model.getHostProjectionGroup())
        self._configuration_ui.configDataCoordinates_fieldChooser.setRegion(dataRegion)
        self._configuration_ui.configDataCoordinates_fieldChooser.setConditional(field_is_managed_coordinates)
        self._configuration_ui.configDataCoordinates_fieldChooser.setField(self._model.getDataCoordinatesField())
        self._configuration_ui.configDataMarkerGroup_fieldChooser.setRegion(dataRegion)
        self._configuration_ui.configDataMarkerGroup_fieldChooser.setNullObjectName("-")
        self._configuration_ui.configDataMarkerGroup_fieldChooser.setConditional(field_is_managed_group)
        self._configuration_ui.configDataMarkerGroup_fieldChooser.setField(self._model.getDataMarkerGroup())
        self._configuration_ui.configDiagnosticLevel_spinBox.setValue(self._dataEmbedder.getDiagnosticLevel())

    def _makeConnectionsConfig(self):
        self._configuration_ui.configFittedCoordinates_fieldChooser.currentIndexChanged.connect(
            self._configFittedCoordinatesFieldChanged)
        self._configuration_ui.configMaterialCoordinates_fieldChooser.currentIndexChanged.connect(
            self._configMaterialCoordinatesFieldChanged)
        self._configuration_ui.configHostMarkerGroup_fieldChooser.currentIndexChanged.connect(
            self._configHostMarkerGroupChanged)
        self._configuration_ui.configHostProjectionGroup_fieldChooser.currentIndexChanged.connect(
            self._configHostProjectionGroupChanged)
        self._configuration_ui.configDataCoordinates_fieldChooser.currentIndexChanged.connect(
            self._configDataCoordinatesFieldChanged)
        self._configuration_ui.configDataMarkerGroup_fieldChooser.currentIndexChanged.connect(
            self._configDataMarkerGroupChanged)
        self._configuration_ui.configDiagnosticLevel_spinBox.valueChanged.connect(
            self._configDiagnosticLevelValueChanged)

    def _configFittedCoordinatesFieldChanged(self, index):
        """
        Callback for change in fitted coordinates field chooser widget.
        """
        self._model.setFittedCoordinatesField(self._configuration_ui.configFittedCoordinates_fieldChooser.getField())

    def _configMaterialCoordinatesFieldChanged(self, index):
        """
        Callback for change in fitted coordinates field chooser widget.
        """
        self._model.setMaterialCoordinatesField(self._configuration_ui.configMaterialCoordinates_fieldChooser.getField())

    def _configHostMarkerGroupChanged(self, index):
        """
        Callback for change in marker group field chooser widget.
        """
        self._model.setHostMarkerGroup(self._configuration_ui.configHostMarkerGroup_fieldChooser.getField())

    def _configHostProjectionGroupChanged(self, index):
        """
        Callback for change in projection group field chooser widget.
        """
        self._model.setHostProjectionGroup(self._configuration_ui.configHostProjectionGroup_fieldChooser.getField())

    def _configDataCoordinatesFieldChanged(self, index):
        """
        Callback for change in data coordinates field chooser widget.
        """
        self._model.setDataCoordinatesField(self._configuration_ui.configDataCoordinates_fieldChooser.getField())

    def _configDataMarkerGroupChanged(self, index):
        """
        Callback for change in data marker group field chooser widget.
        """
        self._model.setDataMarkerGroup(self._configuration_ui.configDataMarkerGroup_fieldChooser.getField())

    def _configDiagnosticLevelValueChanged(self, value):
        self._dataEmbedder.setDiagnosticLevel(value)

    # === display widgets ===

    def _makeConnectionsDisplay(self):
        self._display_settings_ui.displayAxes_checkBox.clicked.connect(self._displayAxesClicked)
        self._display_settings_ui.displayDataMarkerPoints_checkBox.clicked.connect(self._displayDataMarkerPointsClicked)
        self._display_settings_ui.displayDataMarkerNames_checkBox.clicked.connect(self._displayDataMarkerNamesClicked)
        self._display_settings_ui.displayMarkerPoints_checkBox.clicked.connect(self._displayMarkerPointsClicked)
        self._display_settings_ui.displayMarkerNames_checkBox.clicked.connect(self._displayMarkerNamesClicked)
        self._display_settings_ui.displayDataPoints_checkBox.clicked.connect(self._displayDataNodePointsClicked)
        self._display_settings_ui.displayDataLines_checkBox.clicked.connect(self._displayDataLinesClicked)
        self._display_settings_ui.displayDataEmbedded_checkBox.clicked.connect(self._displayDataEmbeddedClicked)
        self._display_settings_ui.displayModelCoordinates_fieldChooser.setRegion(self._model.getHostRegion())
        self._display_settings_ui.displayModelCoordinates_fieldChooser.setNullObjectName("-")
        self._display_settings_ui.displayModelCoordinates_fieldChooser.setConditional(field_is_managed_coordinates)
        self._display_settings_ui.displayModelCoordinates_fieldChooser.setField(self._model.getDisplayModelCoordinatesField())
        self._display_settings_ui.displayModelCoordinates_fieldChooser.currentIndexChanged.connect(
            self._displayModelCoordinatesFieldChanged)
        self._display_settings_ui.displayNodePoints_checkBox.clicked.connect(self._displayNodePointsClicked)
        self._display_settings_ui.displayNodeNumbers_checkBox.clicked.connect(self._displayNodeNumbersClicked)
        self._display_settings_ui.displayElementAxes_checkBox.clicked.connect(self._displayElementAxesClicked)
        self._display_settings_ui.displayElementNumbers_checkBox.clicked.connect(self._displayElementNumbersClicked)
        self._display_settings_ui.displayLines_checkBox.clicked.connect(self._displayLinesClicked)
        self._display_settings_ui.displayLinesExterior_checkBox.clicked.connect(self._displayLinesExteriorClicked)
        self._display_settings_ui.displaySurfaces_checkBox.clicked.connect(self._displaySurfacesClicked)
        self._display_settings_ui.displaySurfacesExterior_checkBox.clicked.connect(self._displaySurfacesExteriorClicked)
        self._display_settings_ui.displaySurfacesTranslucent_checkBox.clicked.connect(self._displaySurfacesTranslucentClicked)
        self._display_settings_ui.displaySurfacesWireframe_checkBox.clicked.connect(self._displaySurfacesWireframeClicked)

    def _updateDisplayWidgets(self):
        """
        Update display widgets to display settings for model graphics display.
        """
        self._display_settings_ui.displayAxes_checkBox.setChecked(self._model.isDisplayAxes())
        self._display_settings_ui.displayDataMarkerPoints_checkBox.setChecked(self._model.isDisplayDataMarkerPoints())
        self._display_settings_ui.displayDataMarkerNames_checkBox.setChecked(self._model.isDisplayDataMarkerNames())
        self._display_settings_ui.displayDataPoints_checkBox.setChecked(self._model.isDisplayDataNodePoints())
        self._display_settings_ui.displayDataLines_checkBox.setChecked(self._model.isDisplayDataLines())
        self._display_settings_ui.displayDataEmbedded_checkBox.setChecked(self._model.isDisplayDataEmbedded())
        self._display_settings_ui.displayModelCoordinates_fieldChooser.setField(self._model.getDisplayModelCoordinatesField())
        self._display_settings_ui.displayMarkerPoints_checkBox.setChecked(self._model.isDisplayMarkerPoints())
        self._display_settings_ui.displayMarkerNames_checkBox.setChecked(self._model.isDisplayMarkerNames())
        self._display_settings_ui.displayNodePoints_checkBox.setChecked(self._model.isDisplayNodePoints())
        self._display_settings_ui.displayNodeNumbers_checkBox.setChecked(self._model.isDisplayNodeNumbers())
        self._display_settings_ui.displayElementNumbers_checkBox.setChecked(self._model.isDisplayElementNumbers())
        self._display_settings_ui.displayElementAxes_checkBox.setChecked(self._model.isDisplayElementAxes())
        self._display_settings_ui.displayLines_checkBox.setChecked(self._model.isDisplayLines())
        self._display_settings_ui.displayLinesExterior_checkBox.setChecked(self._model.isDisplayLinesExterior())
        self._display_settings_ui.displaySurfaces_checkBox.setChecked(self._model.isDisplaySurfaces())
        self._display_settings_ui.displaySurfacesExterior_checkBox.setChecked(self._model.isDisplaySurfacesExterior())
        self._display_settings_ui.displaySurfacesTranslucent_checkBox.setChecked(self._model.isDisplaySurfacesTranslucent())
        self._display_settings_ui.displaySurfacesWireframe_checkBox.setChecked(self._model.isDisplaySurfacesWireframe())

    def _displayAxesClicked(self):
        self._model.setDisplayAxes(self._display_settings_ui.displayAxes_checkBox.isChecked())

    def _displayDataMarkerPointsClicked(self):
        self._model.setDisplayDataMarkerPoints(self._display_settings_ui.displayDataMarkerPoints_checkBox.isChecked())

    def _displayDataMarkerNamesClicked(self):
        self._model.setDisplayDataMarkerNames(self._display_settings_ui.displayDataMarkerNames_checkBox.isChecked())

    def _displayDataNodePointsClicked(self):
        self._model.setDisplayDataNodePoints(self._display_settings_ui.displayNodePoints_checkBox.isChecked())

    def _displayDataLinesClicked(self):
        self._model.setDisplayDataLines(self._display_settings_ui.displayDataLines_checkBox.isChecked())

    def _displayDataEmbeddedClicked(self):
        self._model.setDisplayDataEmbedded(self._display_settings_ui.displayDataEmbedded_checkBox.isChecked())

    def _displayModelCoordinatesFieldChanged(self, index):
        """
        Callback for change in display model coordinates field chooser widget.
        """
        field = self._display_settings_ui.displayModelCoordinates_fieldChooser.getField()
        if field:
            self._model.setDisplayModelCoordinatesField(field)

    def _displayMarkerPointsClicked(self):
        self._model.setDisplayMarkerPoints(self._display_settings_ui.displayMarkerPoints_checkBox.isChecked())

    def _displayMarkerNamesClicked(self):
        self._model.setDisplayMarkerNames(self._display_settings_ui.displayMarkerNames_checkBox.isChecked())

    def _displayNodePointsClicked(self):
        self._model.setDisplayNodePoints(self._display_settings_ui.displayNodePoints_checkBox.isChecked())

    def _displayNodeNumbersClicked(self):
        self._model.setDisplayNodeNumbers(self._display_settings_ui.displayNodeNumbers_checkBox.isChecked())

    def _displayElementAxesClicked(self):
        self._model.setDisplayElementAxes(self._display_settings_ui.displayElementAxes_checkBox.isChecked())

    def _displayElementNumbersClicked(self):
        self._model.setDisplayElementNumbers(self._display_settings_ui.displayElementNumbers_checkBox.isChecked())

    def _displayLinesClicked(self):
        self._model.setDisplayLines(self._display_settings_ui.displayLines_checkBox.isChecked())
        self._autoPerturbLines()

    def _displayLinesExteriorClicked(self):
        self._model.setDisplayLinesExterior(self._display_settings_ui.displayLinesExterior_checkBox.isChecked())

    def _displaySurfacesClicked(self):
        self._model.setDisplaySurfaces(self._display_settings_ui.displaySurfaces_checkBox.isChecked())
        self._autoPerturbLines()

    def _displaySurfacesExteriorClicked(self):
        self._model.setDisplaySurfacesExterior(self._display_settings_ui.displaySurfacesExterior_checkBox.isChecked())

    def _displaySurfacesTranslucentClicked(self):
        self._model.setDisplaySurfacesTranslucent(self._display_settings_ui.displaySurfacesTranslucent_checkBox.isChecked())
        self._autoPerturbLines()

    def _displaySurfacesWireframeClicked(self):
        self._model.setDisplaySurfacesWireframe(self._display_settings_ui.displaySurfacesWireframe_checkBox.isChecked())

    # === general widgets ===

    def _makeConnectionsGeneral(self):
        self._buttons_ui.pushButtonDocumentation.clicked.connect(self._documentationButtonClicked)
        self._buttons_ui.done_pushButton.clicked.connect(self._doneButtonClicked)
        self._buttons_ui.stdViews_pushButton.clicked.connect(self._stdViewsButtonClicked)
        self._buttons_ui.viewAll_pushButton.clicked.connect(self._viewAllButtonClicked)

    def _documentationButtonClicked(self):
        webbrowser.open("https://abi-mapping-tools.readthedocs.io/en/latest/mapclientplugins.dataembedderstep/docs/index.html")

    def _doneButtonClicked(self):
        try:
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)
            self._model.done()
            self._dock_widget.setFloating(False)
            self._doneCallback()
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()

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
        self._data_groups_ui.groups_listView.clicked[QtCore.QModelIndex].connect(self._groupsListItemClicked)

    def _groupsListItemClicked(self, modelIndex):
        """
        Changes current step and possibly changes checked/run status.
        """
        model = modelIndex.model()
        item = model.itemFromIndex(modelIndex)
        groupName = item.text()
        embed = (item.checkState() == QtCore.Qt.CheckState.Checked)
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
        self._groupsItems = QtGui.QStandardItemModel(self._data_groups_ui.groups_listView)
        selectedIndex = None
        groupNames = self._dataEmbedder.getDataGroupNames()
        for groupName in groupNames:
            item = QtGui.QStandardItem(groupName)
            item.setEditable(False)
            item.setCheckable(True)
            item.setCheckState(QtCore.Qt.CheckState.Checked if self._model.isDataGroupEmbed(groupName) else QtCore.Qt.CheckState.Unchecked)
            self._groupsItems.appendRow(item)
            if groupName == self._currentGroupName:
                selectedIndex = self._groupsItems.indexFromItem(item)
        self._data_groups_ui.groups_listView.setModel(self._groupsItems)
        if selectedIndex:
            self._data_groups_ui.groups_listView.setCurrentIndex(selectedIndex)
        self._data_groups_ui.groups_listView.show()
        self._updateGroupWidgets()

    def _updateGroupWidgets(self):
        """
        Update and display widgets for current group
        """
        self._data_groups_ui.groupDimension_lineEdit.setText(
            str(self._dataEmbedder.getDataGroupDimension(self._currentGroupName)) if self._currentGroupName else "")
        self._data_groups_ui.groupSize_lineEdit.setText(str(
            self._dataEmbedder.getDataGroupSize(self._currentGroupName)) if self._currentGroupName else "")
