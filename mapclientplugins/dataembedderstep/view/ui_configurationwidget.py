# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configurationwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QSizePolicy,
    QSpinBox, QWidget)

from cmlibs.widgets.fieldchooserwidget import FieldChooserWidget

class Ui_Configuration(object):
    def setupUi(self, Configuration):
        if not Configuration.objectName():
            Configuration.setObjectName(u"Configuration")
        Configuration.resize(400, 300)
        self.formLayout = QFormLayout(Configuration)
        self.formLayout.setObjectName(u"formLayout")
        self.configFittedCoordinates_label = QLabel(Configuration)
        self.configFittedCoordinates_label.setObjectName(u"configFittedCoordinates_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.configFittedCoordinates_label)

        self.configFittedCoordinates_fieldChooser = FieldChooserWidget(Configuration)
        self.configFittedCoordinates_fieldChooser.setObjectName(u"configFittedCoordinates_fieldChooser")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configFittedCoordinates_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configFittedCoordinates_fieldChooser.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.configFittedCoordinates_fieldChooser)

        self.configMaterialCoordinates_label = QLabel(Configuration)
        self.configMaterialCoordinates_label.setObjectName(u"configMaterialCoordinates_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.configMaterialCoordinates_label)

        self.configMaterialCoordinates_fieldChooser = FieldChooserWidget(Configuration)
        self.configMaterialCoordinates_fieldChooser.setObjectName(u"configMaterialCoordinates_fieldChooser")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.configMaterialCoordinates_fieldChooser)

        self.configHostMarkerGroup_label = QLabel(Configuration)
        self.configHostMarkerGroup_label.setObjectName(u"configHostMarkerGroup_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.configHostMarkerGroup_label)

        self.configHostMarkerGroup_fieldChooser = FieldChooserWidget(Configuration)
        self.configHostMarkerGroup_fieldChooser.setObjectName(u"configHostMarkerGroup_fieldChooser")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.configHostMarkerGroup_fieldChooser)

        self.configHostProjectionGroup_label = QLabel(Configuration)
        self.configHostProjectionGroup_label.setObjectName(u"configHostProjectionGroup_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.configHostProjectionGroup_label)

        self.configHostProjectionGroup_fieldChooser = FieldChooserWidget(Configuration)
        self.configHostProjectionGroup_fieldChooser.setObjectName(u"configHostProjectionGroup_fieldChooser")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.configHostProjectionGroup_fieldChooser)

        self.configDataCoordinates_label = QLabel(Configuration)
        self.configDataCoordinates_label.setObjectName(u"configDataCoordinates_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.configDataCoordinates_label)

        self.configDataCoordinates_fieldChooser = FieldChooserWidget(Configuration)
        self.configDataCoordinates_fieldChooser.setObjectName(u"configDataCoordinates_fieldChooser")
        sizePolicy.setHeightForWidth(self.configDataCoordinates_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configDataCoordinates_fieldChooser.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.configDataCoordinates_fieldChooser)

        self.configDataMarkerGroup_label = QLabel(Configuration)
        self.configDataMarkerGroup_label.setObjectName(u"configDataMarkerGroup_label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.configDataMarkerGroup_label)

        self.configDataMarkerGroup_fieldChooser = FieldChooserWidget(Configuration)
        self.configDataMarkerGroup_fieldChooser.setObjectName(u"configDataMarkerGroup_fieldChooser")
        sizePolicy.setHeightForWidth(self.configDataMarkerGroup_fieldChooser.sizePolicy().hasHeightForWidth())
        self.configDataMarkerGroup_fieldChooser.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.configDataMarkerGroup_fieldChooser)

        self.configDiagnosticLevel_label = QLabel(Configuration)
        self.configDiagnosticLevel_label.setObjectName(u"configDiagnosticLevel_label")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.configDiagnosticLevel_label)

        self.configDiagnosticLevel_spinBox = QSpinBox(Configuration)
        self.configDiagnosticLevel_spinBox.setObjectName(u"configDiagnosticLevel_spinBox")
        self.configDiagnosticLevel_spinBox.setMaximum(2)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.configDiagnosticLevel_spinBox)


        self.retranslateUi(Configuration)

        QMetaObject.connectSlotsByName(Configuration)
    # setupUi

    def retranslateUi(self, Configuration):
        Configuration.setWindowTitle(QCoreApplication.translate("Configuration", u"Configuration", None))
        self.configFittedCoordinates_label.setText(QCoreApplication.translate("Configuration", u"Fitted coordinates:", None))
#if QT_CONFIG(tooltip)
        self.configFittedCoordinates_fieldChooser.setToolTip(QCoreApplication.translate("Configuration", u"<html><head/><body><p>Host coordinates fitted to data, for finding embedded locations.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.configMaterialCoordinates_label.setText(QCoreApplication.translate("Configuration", u"Material coordinates:", None))
#if QT_CONFIG(tooltip)
        self.configMaterialCoordinates_fieldChooser.setToolTip(QCoreApplication.translate("Configuration", u"<html><head/><body><p>Host material coordinates to evaluate and store embedded data locations in.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.configHostMarkerGroup_label.setText(QCoreApplication.translate("Configuration", u"Host marker group:", None))
        self.configHostProjectionGroup_label.setText(QCoreApplication.translate("Configuration", u"Host projection group:", None))
#if QT_CONFIG(tooltip)
        self.configHostProjectionGroup_fieldChooser.setToolTip(QCoreApplication.translate("Configuration", u"<html><head/><body><p>Optional group to project data onto, intersected with fitted group.</p><p>E.g. to limit embedding to a surface group.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.configDataCoordinates_label.setText(QCoreApplication.translate("Configuration", u"Data coordinates:", None))
        self.configDataMarkerGroup_label.setText(QCoreApplication.translate("Configuration", u"Data marker group:", None))
        self.configDiagnosticLevel_label.setText(QCoreApplication.translate("Configuration", u"Diagnostic level:", None))
    # retranslateUi

