# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datagroupswidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QLabel,
    QLineEdit, QListView, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_DataGroups(object):
    def setupUi(self, DataGroups):
        if not DataGroups.objectName():
            DataGroups.setObjectName(u"DataGroups")
        DataGroups.resize(400, 300)
        self.verticalLayout = QVBoxLayout(DataGroups)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groups_listView = QListView(DataGroups)
        self.groups_listView.setObjectName(u"groups_listView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groups_listView.sizePolicy().hasHeightForWidth())
        self.groups_listView.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.groups_listView)

        self.groupSettings_groupBox = QGroupBox(DataGroups)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupSize_lineEdit.sizePolicy().hasHeightForWidth())
        self.groupSize_lineEdit.setSizePolicy(sizePolicy1)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.groupSize_lineEdit)


        self.verticalLayout.addWidget(self.groupSettings_groupBox)


        self.retranslateUi(DataGroups)

        QMetaObject.connectSlotsByName(DataGroups)
    # setupUi

    def retranslateUi(self, DataGroups):
        DataGroups.setWindowTitle(QCoreApplication.translate("DataGroups", u"Data Groups", None))
#if QT_CONFIG(tooltip)
        self.groups_listView.setToolTip(QCoreApplication.translate("DataGroups", u"<html><head/><body><p>Tick data groups to embed.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupSettings_groupBox.setTitle(QCoreApplication.translate("DataGroups", u"Group settings:", None))
        self.groupDimension_label.setText(QCoreApplication.translate("DataGroups", u"Dimension:", None))
        self.groupSize_label.setText(QCoreApplication.translate("DataGroups", u"Size:", None))
    # retranslateUi

