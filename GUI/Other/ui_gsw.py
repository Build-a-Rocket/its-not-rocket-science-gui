# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gsw.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLayout,
    QSizePolicy, QTextEdit, QWidget)

from pyqtgraph import PlotWidget

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(947, 612)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"bar.ico", QSize(), QIcon.Normal, QIcon.Off)
        Main.setWindowIcon(icon)
        Main.setAutoFillBackground(False)
        self.gridLayout_2 = QGridLayout(Main)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.outputBox = QTextEdit(Main)
        self.outputBox.setObjectName(u"outputBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.outputBox.sizePolicy().hasHeightForWidth())
        self.outputBox.setSizePolicy(sizePolicy1)
        self.outputBox.setReadOnly(True)

        self.horizontalLayout.addWidget(self.outputBox)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.accelGraph = PlotWidget(Main)
        self.accelGraph.setObjectName(u"accelGraph")
        self.accelGraph.setStyleSheet(u"QWidget\n"
"{\n"
"background-color: rgb(0, 255, 255)\n"
"}")

        self.gridLayout.addWidget(self.accelGraph, 1, 0, 1, 1)

        self.altitudeGraph = PlotWidget(Main)
        self.altitudeGraph.setObjectName(u"altitudeGraph")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.altitudeGraph.sizePolicy().hasHeightForWidth())
        self.altitudeGraph.setSizePolicy(sizePolicy2)
        self.altitudeGraph.setStyleSheet(u"QWidget\n"
"{\n"
"background-color: rgb(0, 255, 255)\n"
"}")

        self.gridLayout.addWidget(self.altitudeGraph, 0, 0, 1, 1)

        self.tempGraph = PlotWidget(Main)
        self.tempGraph.setObjectName(u"tempGraph")
        self.tempGraph.setStyleSheet(u"QWidget\n"
"{\n"
"background-color: rgb(0, 255, 255)\n"
"}")

        self.gridLayout.addWidget(self.tempGraph, 0, 1, 1, 1)

        self.gyroGraph = PlotWidget(Main)
        self.gyroGraph.setObjectName(u"gyroGraph")
        sizePolicy2.setHeightForWidth(self.gyroGraph.sizePolicy().hasHeightForWidth())
        self.gyroGraph.setSizePolicy(sizePolicy2)
        self.gyroGraph.setStyleSheet(u"QWidget\n"
"{\n"
"background-color: rgb(0, 255, 255)\n"
"}")

        self.gridLayout.addWidget(self.gyroGraph, 1, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Build-a-Rocket PyGSW", None))
    # retranslateUi

