
"""
MAP Client Plugin Step
"""
import json

from PySide6 import QtWidgets, QtCore

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.dataembedderstep.configuredialog import ConfigureDialog
from mapclientplugins.dataembedderstep.model.dataembeddermodel import DataEmbedderModel
from mapclientplugins.dataembedderstep.view.dataembedderwidget import DataEmbedderWidget


class DataEmbedderStep(WorkflowStepMountPoint):
    """
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    """

    def __init__(self, location):
        super(DataEmbedderStep, self).__init__('DataEmbedder', location)
        self._configured = False # A step cannot be executed until it has been configured.
        self._category = 'Utility'
        # Add any other initialisation code here:
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'))
        # Port data:
        self._port0_inputZincScaffoldFile = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        self._port1_inputZincFittedGeometryFile = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        self._port2_inputZincDataFile = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        self._port3_outputZincDataFile = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        # Config:
        self._config = {}
        self._config['identifier'] = ''
        self._model = None
        self._view = None

    def execute(self):
        """
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        """
        # Put your execute step code here before calling the '_doneExecution' method.
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)
        self._model = DataEmbedderModel(self._port0_inputZincScaffoldFile, self._port1_inputZincFittedGeometryFile,
                                        self._port2_inputZincDataFile, self._location, self._config['identifier'])
        self._view = DataEmbedderWidget(self._model)
        self._view.registerDoneExecution(self._doneExecution)
        self._setCurrentWidget(self._view)
        QtWidgets.QApplication.restoreOverrideCursor()

    def setPortData(self, index, dataIn):
        """
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.

        :param index: Index of the port to return.
        :param dataIn: The data to set for the port at the given index.
        """
        if index == 0:
            self._port0_inputZincScaffoldFile = dataIn
            # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        elif index == 1:
            self._port1_inputZincFittedGeometryFile = dataIn
            # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location
        elif index == 2:
            self._port2_inputZincDataFile = dataIn  # http://physiomeproject.org/workflow/1.0/rdf-schema#file_location

    def getPortData(self, index):
        """
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.

        :param index: Index of the port to return.
        """
        return self._model.getOutputModelFileName()

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """
        dlg = ConfigureDialog(self._main_window)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._config['identifier']

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._config['identifier'] = identifier

    def serialize(self):
        """
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.

        :param string: JSON representation of the configuration in a string.
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()
