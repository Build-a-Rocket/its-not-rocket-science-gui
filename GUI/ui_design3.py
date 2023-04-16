# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design3.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLayout, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(725, 544)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.GYRO = PlotWidget(Form)
        self.GYRO.setObjectName(u"GYRO")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GYRO.sizePolicy().hasHeightForWidth())
        self.GYRO.setSizePolicy(sizePolicy)
        self.GYRO.setStyleSheet(u"QWidget\n"
"{\n"
"background-color: rgb(0, 255, 255)\n"
"}")

        self.gridLayout.addWidget(self.GYRO, 0, 2, 1, 1)

        self.MODE3D = QFrame(Form)
        self.MODE3D.setObjectName(u"MODE3D")
        sizePolicy.setHeightForWidth(self.MODE3D.sizePolicy().hasHeightForWidth())
        self.MODE3D.setSizePolicy(sizePolicy)
        self.MODE3D.setFrameShape(QFrame.StyledPanel)
        self.MODE3D.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.MODE3D, 2, 0, 1, 1)

        self.VIDEO = QFrame(Form)
        self.VIDEO.setObjectName(u"VIDEO")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.VIDEO.sizePolicy().hasHeightForWidth())
        self.VIDEO.setSizePolicy(sizePolicy1)
        self.VIDEO.setFrameShape(QFrame.StyledPanel)
        self.VIDEO.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.VIDEO, 1, 1, 1, 1)

        self.LOCATION3D = QFrame(Form)
        self.LOCATION3D.setObjectName(u"LOCATION3D")
        sizePolicy.setHeightForWidth(self.LOCATION3D.sizePolicy().hasHeightForWidth())
        self.LOCATION3D.setSizePolicy(sizePolicy)
        self.LOCATION3D.setFrameShape(QFrame.StyledPanel)
        self.LOCATION3D.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.LOCATION3D, 0, 1, 1, 1)

        self.SETTINGS = QVBoxLayout()
        self.SETTINGS.setObjectName(u"SETTINGS")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.CALIBRATE_Y = QPushButton(Form)
        self.CALIBRATE_Y.setObjectName(u"CALIBRATE_Y")
        sizePolicy1.setHeightForWidth(self.CALIBRATE_Y.sizePolicy().hasHeightForWidth())
        self.CALIBRATE_Y.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.CALIBRATE_Y, 1, 0, 1, 1)

        self.CALIBRATE_Z = QPushButton(Form)
        self.CALIBRATE_Z.setObjectName(u"CALIBRATE_Z")
        sizePolicy1.setHeightForWidth(self.CALIBRATE_Z.sizePolicy().hasHeightForWidth())
        self.CALIBRATE_Z.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.CALIBRATE_Z, 0, 0, 1, 1)

        self.CALIBRATE_ALT = QPushButton(Form)
        self.CALIBRATE_ALT.setObjectName(u"CALIBRATE_ALT")
        self.CALIBRATE_ALT.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.CALIBRATE_ALT.sizePolicy().hasHeightForWidth())
        self.CALIBRATE_ALT.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.CALIBRATE_ALT, 1, 1, 1, 1)

        self.CALIBRATE_X = QPushButton(Form)
        self.CALIBRATE_X.setObjectName(u"CALIBRATE_X")
        sizePolicy1.setHeightForWidth(self.CALIBRATE_X.sizePolicy().hasHeightForWidth())
        self.CALIBRATE_X.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.CALIBRATE_X, 0, 1, 1, 1)


        self.SETTINGS.addLayout(self.gridLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.UPDATEPARAMS = QPushButton(Form)
        self.UPDATEPARAMS.setObjectName(u"UPDATEPARAMS")
        sizePolicy1.setHeightForWidth(self.UPDATEPARAMS.sizePolicy().hasHeightForWidth())
        self.UPDATEPARAMS.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.UPDATEPARAMS)

        self.UPDATEPARAMS_2 = QPushButton(Form)
        self.UPDATEPARAMS_2.setObjectName(u"UPDATEPARAMS_2")
        sizePolicy1.setHeightForWidth(self.UPDATEPARAMS_2.sizePolicy().hasHeightForWidth())
        self.UPDATEPARAMS_2.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.UPDATEPARAMS_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.UPDATEPARAMS_3 = QPushButton(Form)
        self.UPDATEPARAMS_3.setObjectName(u"UPDATEPARAMS_3")
        sizePolicy1.setHeightForWidth(self.UPDATEPARAMS_3.sizePolicy().hasHeightForWidth())
        self.UPDATEPARAMS_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.UPDATEPARAMS_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.SETTINGS.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.SETTINGS, 2, 2, 1, 1)

        self.TEMPERATURE = PlotWidget(Form)
        self.TEMPERATURE.setObjectName(u"TEMPERATURE")
        sizePolicy.setHeightForWidth(self.TEMPERATURE.sizePolicy().hasHeightForWidth())
        self.TEMPERATURE.setSizePolicy(sizePolicy)
        self.TEMPERATURE.setStyleSheet(u"QWidget\n"
"{\n"
"background-color: rgb(0, 255, 255)\n"
"}")

        self.gridLayout.addWidget(self.TEMPERATURE, 1, 2, 1, 1)

        self.ACCELERATION = PlotWidget(Form)
        self.ACCELERATION.setObjectName(u"ACCELERATION")
        sizePolicy.setHeightForWidth(self.ACCELERATION.sizePolicy().hasHeightForWidth())
        self.ACCELERATION.setSizePolicy(sizePolicy)
        self.ACCELERATION.setStyleSheet(u"QWidget\n"
"{\n"
"background-color: rgb(0, 255, 255)\n"
"}")

        self.gridLayout.addWidget(self.ACCELERATION, 0, 0, 1, 1)

        self.ALTITUDE = PlotWidget(Form)
        self.ALTITUDE.setObjectName(u"ALTITUDE")
        sizePolicy.setHeightForWidth(self.ALTITUDE.sizePolicy().hasHeightForWidth())
        self.ALTITUDE.setSizePolicy(sizePolicy)
        self.ALTITUDE.setStyleSheet(u"QWidget\n"
"{\n"
"background-color: rgb(0, 255, 255)\n"
"}")

        self.gridLayout.addWidget(self.ALTITUDE, 1, 0, 1, 1)

        self.RAW = QTextEdit(Form)
        self.RAW.setObjectName(u"RAW")
        sizePolicy.setHeightForWidth(self.RAW.sizePolicy().hasHeightForWidth())
        self.RAW.setSizePolicy(sizePolicy)
        self.RAW.setReadOnly(True)

        self.gridLayout.addWidget(self.RAW, 2, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.CALIBRATE_Y.setText(QCoreApplication.translate("Form", u"Calibrate Y", None))
        self.CALIBRATE_Z.setText(QCoreApplication.translate("Form", u"Calibrate Z", None))
        self.CALIBRATE_ALT.setText(QCoreApplication.translate("Form", u"Calibrate ALT", None))
        self.CALIBRATE_X.setText(QCoreApplication.translate("Form", u"Calibrate X", None))
        self.UPDATEPARAMS.setText(QCoreApplication.translate("Form", u"Update Parameters", None))
        self.UPDATEPARAMS_2.setText(QCoreApplication.translate("Form", u"Start CSV log", None))
        self.UPDATEPARAMS_3.setText(QCoreApplication.translate("Form", u"Select COM", None))
    # retranslateUi

