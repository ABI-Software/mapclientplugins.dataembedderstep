# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataembedderwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget
from opencmiss.zincwidgets.fieldchooserwidget import FieldChooserWidget


class Ui_DataEmbedderWidget(object):
    def setupUi(self, DataEmbedderWidget):
        if not DataEmbedderWidget.objectName():
            DataEmbedderWidget.setObjectName(u"DataEmbedderWidget")
        DataEmbedderWidget.resize(1718, 1122)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DataEmbedderWidget.sizePolicy().hasHeightForWidth())
        DataEmbedderWidget.setSizePolicy(sizePolicy)
        DataEmbedderWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(DataEmbedderWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dockWidget = QDockWidget(DataEmbedderWidget)
        self.dockWidget.setObjectName(u"dockWidget")
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.config_groupBox = QGroupBox(self.dockWidgetContents)
        self.config_groupBox.setObjectName(u"config_groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.config_groupBox.sizePolicy().hasHeightForWidth())
        self.config_groupBox.setSizePolicy(sizePolicy2)
        self.formLayout = QFormLayout(self.config_groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.configFittedCoordinates_label = QLabel(self.config_groupBox)
        self.configFittedCoordinates_label.setObjectName(u"configFittedCoordinates_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.configFittedCoordinates_label)

        self.configFittedCoordinates_fieldChooser = FieldChooserWidget(self.config_groupBox)
        self.configFittedCoordinates_fieldChooser.setObjectName(u"configFittedCoordinates_fieldChooser")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.configFittedCoordinates_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configFittedCoordinates_fieldChooser.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.configFittedCoordinates_fieldChooser)

        self.configDataCoordinates_label = QLabel(self.config_groupBox)
        self.configDataCoordinates_label.setObjectName(u"configDataCoordinates_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.configDataCoordinates_label)

        self.configDataCoordinates_fieldChooser = FieldChooserWidget(self.config_groupBox)
        self.configDataCoordinates_fieldChooser.setObjectName(u"configDataCoordinates_fieldChooser")
        sizePolicy3.setHeightForWidth(self.configDataCoordinates_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configDataCoordinates_fieldChooser.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.configDataCoordinates_fieldChooser)

        self.configDiagnosticLevel_spinBox = QSpinBox(self.config_groupBox)
        self.configDiagnosticLevel_spinBox.setObjectName(u"configDiagnosticLevel_spinBox")
        self.configDiagnosticLevel_spinBox.setMaximum(2)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.configDiagnosticLevel_spinBox)

        self.configDiagnosticLevel_label = QLabel(self.config_groupBox)
        self.configDiagnosticLevel_label.setObjectName(u"configDiagnosticLevel_label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.configDiagnosticLevel_label)

        self.configDataMarkerGroup_label = QLabel(self.config_groupBox)
        self.configDataMarkerGroup_label.setObjectName(u"configDataMarkerGroup_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.configDataMarkerGroup_label)

        self.configDataMarkerGroup_fieldChooser = FieldChooserWidget(self.config_groupBox)
        self.configDataMarkerGroup_fieldChooser.setObjectName(u"configDataMarkerGroup_fieldChooser")
        sizePolicy3.setHeightForWidth(self.configDataMarkerGroup_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configDataMarkerGroup_fieldChooser.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.configDataMarkerGroup_fieldChooser)

        self.configMaterialCoordinates_label = QLabel(self.config_groupBox)
        self.configMaterialCoordinates_label.setObjectName(u"configMaterialCoordinates_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.configMaterialCoordinates_label)

        self.configMaterialCoordinates_fieldChooser = FieldChooserWidget(self.config_groupBox)
        self.configMaterialCoordinates_fieldChooser.setObjectName(u"configMaterialCoordinates_fieldChooser")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.configMaterialCoordinates_fieldChooser)

        self.configHostMarkerGroup_label = QLabel(self.config_groupBox)
        self.configHostMarkerGroup_label.setObjectName(u"configHostMarkerGroup_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.configHostMarkerGroup_label)

        self.configHostMarkerGroup_fieldChooser = FieldChooserWidget(self.config_groupBox)
        self.configHostMarkerGroup_fieldChooser.setObjectName(u"configHostMarkerGroup_fieldChooser")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.configHostMarkerGroup_fieldChooser)


        self.verticalLayout.addWidget(self.config_groupBox)

        self.groups_groupBox = QGroupBox(self.dockWidgetContents)
        self.groups_groupBox.setObjectName(u"groups_groupBox")
        sizePolicy.setHeightForWidth(self.groups_groupBox.sizePolicy().hasHeightForWidth())
        self.groups_groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groups_groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groups_listView = QListView(self.groups_groupBox)
        self.groups_listView.setObjectName(u"groups_listView")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groups_listView.sizePolicy().hasHeightForWidth())
        self.groups_listView.setSizePolicy(sizePolicy4)

        self.verticalLayout_2.addWidget(self.groups_listView)

        self.groupSettings_groupBox = QGroupBox(self.groups_groupBox)
        self.groupSettings_groupBox.setObjectName(u"groupSettings_groupBox")
        self.formLayout_3 = QFormLayout(self.groupSettings_groupBox)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.groupDimension_label = QLabel(self.groupSettings_groupBox)
        self.groupDimension_label.setObjectName(u"groupDimension_label")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.groupDimension_label)

        self.groupDimension_lineEdit = QLineEdit(self.groupSettings_groupBox)
        self.groupDimension_lineEdit.setObjectName(u"groupDimension_lineEdit")
        self.groupDimension_lineEdit.setEnabled(False)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.groupDimension_lineEdit)

        self.groupSize_label = QLabel(self.groupSettings_groupBox)
        self.groupSize_label.setObjectName(u"groupSize_label")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.groupSize_label)

        self.groupSize_lineEdit = QLineEdit(self.groupSettings_groupBox)
        self.groupSize_lineEdit.setObjectName(u"groupSize_lineEdit")
        self.groupSize_lineEdit.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.groupSize_lineEdit.sizePolicy().hasHeightForWidth())
        self.groupSize_lineEdit.setSizePolicy(sizePolicy3)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.groupSize_lineEdit)


        self.verticalLayout_2.addWidget(self.groupSettings_groupBox)


        self.verticalLayout.addWidget(self.groups_groupBox)

        self.display_groupBox = QGroupBox(self.dockWidgetContents)
        self.display_groupBox.setObjectName(u"display_groupBox")
        sizePolicy.setHeightForWidth(self.display_groupBox.sizePolicy().hasHeightForWidth())
        self.display_groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.display_groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.displayMisc_frame = QFrame(self.display_groupBox)
        self.displayMisc_frame.setObjectName(u"displayMisc_frame")
        self.displayMisc_frame.setFrameShape(QFrame.StyledPanel)
        self.displayMisc_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.displayMisc_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.displayAxes_checkBox = QCheckBox(self.displayMisc_frame)
        self.displayAxes_checkBox.setObjectName(u"displayAxes_checkBox")

        self.horizontalLayout_8.addWidget(self.displayAxes_checkBox)

        self.displaytMisc_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.displaytMisc_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displayMisc_frame)

        self.displayDataMarker_frame = QFrame(self.display_groupBox)
        self.displayDataMarker_frame.setObjectName(u"displayDataMarker_frame")
        self.displayDataMarker_frame.setFrameShape(QFrame.StyledPanel)
        self.displayDataMarker_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.displayDataMarker_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.displayDataMarkerPoints_checkBox = QCheckBox(self.displayDataMarker_frame)
        self.displayDataMarkerPoints_checkBox.setObjectName(u"displayDataMarkerPoints_checkBox")

        self.horizontalLayout_7.addWidget(self.displayDataMarkerPoints_checkBox)

        self.displayDataMarkerNames_checkBox = QCheckBox(self.displayDataMarker_frame)
        self.displayDataMarkerNames_checkBox.setObjectName(u"displayDataMarkerNames_checkBox")

        self.horizontalLayout_7.addWidget(self.displayDataMarkerNames_checkBox)

        self.displayDataMarker_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.displayDataMarker_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displayDataMarker_frame)

        self.displayData_frame = QFrame(self.display_groupBox)
        self.displayData_frame.setObjectName(u"displayData_frame")
        self.displayData_frame.setFrameShape(QFrame.StyledPanel)
        self.displayData_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.displayData_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.displayDataNodePoints_checkBox = QCheckBox(self.displayData_frame)
        self.displayDataNodePoints_checkBox.setObjectName(u"displayDataNodePoints_checkBox")

        self.horizontalLayout_10.addWidget(self.displayDataNodePoints_checkBox)

        self.displayDataLines_checkBox = QCheckBox(self.displayData_frame)
        self.displayDataLines_checkBox.setObjectName(u"displayDataLines_checkBox")

        self.horizontalLayout_10.addWidget(self.displayDataLines_checkBox)

        self.displayDataEmbedded_checkBox = QCheckBox(self.displayData_frame)
        self.displayDataEmbedded_checkBox.setObjectName(u"displayDataEmbedded_checkBox")

        self.horizontalLayout_10.addWidget(self.displayDataEmbedded_checkBox)

        self.displayData_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.displayData_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displayData_frame)

        self.displayModelCoordinates_frame = QFrame(self.display_groupBox)
        self.displayModelCoordinates_frame.setObjectName(u"displayModelCoordinates_frame")
        self.displayModelCoordinates_frame.setFrameShape(QFrame.StyledPanel)
        self.displayModelCoordinates_frame.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.displayModelCoordinates_frame)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.displayModelCoordinates_label = QLabel(self.displayModelCoordinates_frame)
        self.displayModelCoordinates_label.setObjectName(u"displayModelCoordinates_label")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.displayModelCoordinates_label)

        self.displayModelCoordinates_fieldChooser = FieldChooserWidget(self.displayModelCoordinates_frame)
        self.displayModelCoordinates_fieldChooser.setObjectName(u"displayModelCoordinates_fieldChooser")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.displayModelCoordinates_fieldChooser)


        self.verticalLayout_7.addWidget(self.displayModelCoordinates_frame)

        self.displayMarker_frame = QFrame(self.display_groupBox)
        self.displayMarker_frame.setObjectName(u"displayMarker_frame")
        self.displayMarker_frame.setFrameShape(QFrame.StyledPanel)
        self.displayMarker_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.displayMarker_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.displayMarkerPoints_checkBox = QCheckBox(self.displayMarker_frame)
        self.displayMarkerPoints_checkBox.setObjectName(u"displayMarkerPoints_checkBox")

        self.horizontalLayout_9.addWidget(self.displayMarkerPoints_checkBox)

        self.displayMarkerNames_checkBox = QCheckBox(self.displayMarker_frame)
        self.displayMarkerNames_checkBox.setObjectName(u"displayMarkerNames_checkBox")

        self.horizontalLayout_9.addWidget(self.displayMarkerNames_checkBox)

        self.displayMarker_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.displayMarker_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displayMarker_frame)

        self.displayNodes_frame = QFrame(self.display_groupBox)
        self.displayNodes_frame.setObjectName(u"displayNodes_frame")
        self.displayNodes_frame.setFrameShape(QFrame.StyledPanel)
        self.displayNodes_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.displayNodes_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.displayNodePoints_checkBox = QCheckBox(self.displayNodes_frame)
        self.displayNodePoints_checkBox.setObjectName(u"displayNodePoints_checkBox")

        self.horizontalLayout_6.addWidget(self.displayNodePoints_checkBox)

        self.displayNodeNumbers_checkBox = QCheckBox(self.displayNodes_frame)
        self.displayNodeNumbers_checkBox.setObjectName(u"displayNodeNumbers_checkBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.displayNodeNumbers_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeNumbers_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_6.addWidget(self.displayNodeNumbers_checkBox)

        self.displayNodes_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.displayNodes_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displayNodes_frame)

        self.displayElements_frame = QFrame(self.display_groupBox)
        self.displayElements_frame.setObjectName(u"displayElements_frame")
        self.displayElements_frame.setFrameShape(QFrame.StyledPanel)
        self.displayElements_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.displayElements_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.displayElementNumbers_checkBox = QCheckBox(self.displayElements_frame)
        self.displayElementNumbers_checkBox.setObjectName(u"displayElementNumbers_checkBox")

        self.horizontalLayout_4.addWidget(self.displayElementNumbers_checkBox)

        self.displayElementAxes_checkBox = QCheckBox(self.displayElements_frame)
        self.displayElementAxes_checkBox.setObjectName(u"displayElementAxes_checkBox")
        sizePolicy5.setHeightForWidth(self.displayElementAxes_checkBox.sizePolicy().hasHeightForWidth())
        self.displayElementAxes_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_4.addWidget(self.displayElementAxes_checkBox)

        self.displayElements_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.displayElements_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displayElements_frame)

        self.displayLines_frame = QFrame(self.display_groupBox)
        self.displayLines_frame.setObjectName(u"displayLines_frame")
        self.displayLines_frame.setFrameShape(QFrame.StyledPanel)
        self.displayLines_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.displayLines_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.displayLines_checkBox = QCheckBox(self.displayLines_frame)
        self.displayLines_checkBox.setObjectName(u"displayLines_checkBox")

        self.horizontalLayout_5.addWidget(self.displayLines_checkBox)

        self.displayLinesExterior_checkBox = QCheckBox(self.displayLines_frame)
        self.displayLinesExterior_checkBox.setObjectName(u"displayLinesExterior_checkBox")
        sizePolicy5.setHeightForWidth(self.displayLinesExterior_checkBox.sizePolicy().hasHeightForWidth())
        self.displayLinesExterior_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.displayLinesExterior_checkBox)

        self.displayLines_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.displayLines_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displayLines_frame)

        self.displaySurfaces_frame = QFrame(self.display_groupBox)
        self.displaySurfaces_frame.setObjectName(u"displaySurfaces_frame")
        self.displaySurfaces_frame.setFrameShape(QFrame.StyledPanel)
        self.displaySurfaces_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.displaySurfaces_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.displaySurfaces_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfaces_checkBox.setObjectName(u"displaySurfaces_checkBox")

        self.horizontalLayout_3.addWidget(self.displaySurfaces_checkBox)

        self.displaySurfacesExterior_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesExterior_checkBox.setObjectName(u"displaySurfacesExterior_checkBox")
        sizePolicy5.setHeightForWidth(self.displaySurfacesExterior_checkBox.sizePolicy().hasHeightForWidth())
        self.displaySurfacesExterior_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.displaySurfacesExterior_checkBox)

        self.displaySurfacesTranslucent_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesTranslucent_checkBox.setObjectName(u"displaySurfacesTranslucent_checkBox")
        sizePolicy5.setHeightForWidth(self.displaySurfacesTranslucent_checkBox.sizePolicy().hasHeightForWidth())
        self.displaySurfacesTranslucent_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.displaySurfacesTranslucent_checkBox)

        self.displaySurfacesWireframe_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesWireframe_checkBox.setObjectName(u"displaySurfacesWireframe_checkBox")
        sizePolicy5.setHeightForWidth(self.displaySurfacesWireframe_checkBox.sizePolicy().hasHeightForWidth())
        self.displaySurfacesWireframe_checkBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.displaySurfacesWireframe_checkBox)

        self.displaySurfaces_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.displaySurfaces_horizontalSpacer)


        self.verticalLayout_7.addWidget(self.displaySurfaces_frame)


        self.verticalLayout.addWidget(self.display_groupBox)

        self.bottom_frame = QFrame(self.dockWidgetContents)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.pushButtonDocumentation = QPushButton(self.bottom_frame)
        self.pushButtonDocumentation.setObjectName(u"pushButtonDocumentation")

        self.horizontalLayout_2.addWidget(self.pushButtonDocumentation)

        self.viewAll_pushButton = QPushButton(self.bottom_frame)
        self.viewAll_pushButton.setObjectName(u"viewAll_pushButton")

        self.horizontalLayout_2.addWidget(self.viewAll_pushButton)

        self.stdViews_pushButton = QPushButton(self.bottom_frame)
        self.stdViews_pushButton.setObjectName(u"stdViews_pushButton")

        self.horizontalLayout_2.addWidget(self.stdViews_pushButton)

        self.done_pushButton = QPushButton(self.bottom_frame)
        self.done_pushButton.setObjectName(u"done_pushButton")
        sizePolicy5.setHeightForWidth(self.done_pushButton.sizePolicy().hasHeightForWidth())
        self.done_pushButton.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.done_pushButton)


        self.verticalLayout.addWidget(self.bottom_frame)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.horizontalLayout.addWidget(self.dockWidget)

        self.sceneviewerwidget = SceneviewerWidget(DataEmbedderWidget)
        self.sceneviewerwidget.setObjectName(u"sceneviewerwidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.sceneviewerwidget.sizePolicy().hasHeightForWidth())
        self.sceneviewerwidget.setSizePolicy(sizePolicy6)

        self.horizontalLayout.addWidget(self.sceneviewerwidget)


        self.retranslateUi(DataEmbedderWidget)

        QMetaObject.connectSlotsByName(DataEmbedderWidget)
    # setupUi

    def retranslateUi(self, DataEmbedderWidget):
        DataEmbedderWidget.setWindowTitle(QCoreApplication.translate("DataEmbedderWidget", u"Data Embedder", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("DataEmbedderWidget", u"Control Panel", None))
        self.config_groupBox.setTitle(QCoreApplication.translate("DataEmbedderWidget", u"Configuration", None))
        self.configFittedCoordinates_label.setText(QCoreApplication.translate("DataEmbedderWidget", u"Fitted coordinates:", None))
#if QT_CONFIG(tooltip)
        self.configFittedCoordinates_fieldChooser.setToolTip(QCoreApplication.translate("DataEmbedderWidget", u"<html><head/><body><p>Host coordinates fitted to data, for finding embedded locations.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.configDataCoordinates_label.setText(QCoreApplication.translate("DataEmbedderWidget", u"Data coordinates:", None))
        self.configDiagnosticLevel_label.setText(QCoreApplication.translate("DataEmbedderWidget", u"Diagnostic level:", None))
        self.configDataMarkerGroup_label.setText(QCoreApplication.translate("DataEmbedderWidget", u"Data marker group:", None))
        self.configMaterialCoordinates_label.setText(QCoreApplication.translate("DataEmbedderWidget", u"Material coordinates:", None))
#if QT_CONFIG(tooltip)
        self.configMaterialCoordinates_fieldChooser.setToolTip(QCoreApplication.translate("DataEmbedderWidget", u"<html><head/><body><p>Host material coordinates to evaluate and store embedded data locations in.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.configHostMarkerGroup_label.setText(QCoreApplication.translate("DataEmbedderWidget", u"Host marker group:", None))
        self.groups_groupBox.setTitle(QCoreApplication.translate("DataEmbedderWidget", u"Data groups:", None))
#if QT_CONFIG(tooltip)
        self.groups_listView.setToolTip(QCoreApplication.translate("DataEmbedderWidget", u"<html><head/><body><p>Tick data groups to embed.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupSettings_groupBox.setTitle(QCoreApplication.translate("DataEmbedderWidget", u"Group settings:", None))
        self.groupDimension_label.setText(QCoreApplication.translate("DataEmbedderWidget", u"Dimension:", None))
        self.groupSize_label.setText(QCoreApplication.translate("DataEmbedderWidget", u"Size:", None))
        self.display_groupBox.setTitle(QCoreApplication.translate("DataEmbedderWidget", u"Display:", None))
        self.displayAxes_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Axes", None))
        self.displayDataMarkerPoints_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Data marker points", None))
        self.displayDataMarkerNames_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Data marker names", None))
        self.displayDataNodePoints_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Data node points", None))
        self.displayDataLines_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Data lines", None))
#if QT_CONFIG(tooltip)
        self.displayDataEmbedded_checkBox.setToolTip(QCoreApplication.translate("DataEmbedderWidget", u"<html><head/><body><p>Show data embedded in model coordinates.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.displayDataEmbedded_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Data embedded", None))
        self.displayModelCoordinates_label.setText(QCoreApplication.translate("DataEmbedderWidget", u"Model coordinates:", None))
#if QT_CONFIG(tooltip)
        self.displayModelCoordinates_fieldChooser.setToolTip(QCoreApplication.translate("DataEmbedderWidget", u"<html><head/><body><p>Coordinates to display host model and embedded data in.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.displayMarkerPoints_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Marker points", None))
        self.displayMarkerNames_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Marker names", None))
        self.displayNodePoints_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Node points", None))
        self.displayNodeNumbers_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Node numbers", None))
        self.displayElementNumbers_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Element numbers", None))
        self.displayElementAxes_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Element axes", None))
        self.displayLines_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Lines", None))
        self.displayLinesExterior_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Exterior", None))
        self.displaySurfaces_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Surfaces", None))
        self.displaySurfacesExterior_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Exterior", None))
        self.displaySurfacesTranslucent_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Transluc.", None))
        self.displaySurfacesWireframe_checkBox.setText(QCoreApplication.translate("DataEmbedderWidget", u"Wireframe", None))
        self.pushButtonDocumentation.setText(QCoreApplication.translate("DataEmbedderWidget", u"Online Documentation", None))
        self.viewAll_pushButton.setText(QCoreApplication.translate("DataEmbedderWidget", u"View All", None))
#if QT_CONFIG(tooltip)
        self.stdViews_pushButton.setToolTip(QCoreApplication.translate("DataEmbedderWidget", u"<html><head/><body><p>Cycle standard views:<br/>x-y  x-z  y-z</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.stdViews_pushButton.setText(QCoreApplication.translate("DataEmbedderWidget", u"Std. Views", None))
        self.done_pushButton.setText(QCoreApplication.translate("DataEmbedderWidget", u"Done", None))
    # retranslateUi

