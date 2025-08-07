# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataembedderwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QVBoxLayout,
    QWidget)

from cmlibs.widgets.sceneviewerwidget import SceneviewerWidget

class Ui_DataEmbedderWidget(object):
    def setupUi(self, DataEmbedderWidget):
        if not DataEmbedderWidget.objectName():
            DataEmbedderWidget.setObjectName(u"DataEmbedderWidget")
        DataEmbedderWidget.resize(800, 600)
        self.centralwidget = QWidget(DataEmbedderWidget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sceneviewerwidget = SceneviewerWidget(self.centralwidget)
        self.sceneviewerwidget.setObjectName(u"sceneviewerwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sceneviewerwidget.sizePolicy().hasHeightForWidth())
        self.sceneviewerwidget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.sceneviewerwidget)

        DataEmbedderWidget.setCentralWidget(self.centralwidget)

        self.retranslateUi(DataEmbedderWidget)

        QMetaObject.connectSlotsByName(DataEmbedderWidget)
    # setupUi

    def retranslateUi(self, DataEmbedderWidget):
        DataEmbedderWidget.setWindowTitle(QCoreApplication.translate("DataEmbedderWidget", u"Data Embedder", None))
    # retranslateUi

