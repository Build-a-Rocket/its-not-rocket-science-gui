import random

from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit
from PyQt6 import uic, QtCore
from pyqtgraph import PlotWidget
from serial import Serial, unicode
from PIL import Image
from serial_thread import SerialThread
from tele_graph import TelemetryGraph


class UI(QWidget):

    def __init__(self):
        super().__init__()

        # loading the ui file with uic module
        uic.loadUi('E:\PythonProjects\Rocketgui\its-not-rocket-science-gui\GUI\Other\gsw.ui', self)

        # Initiate serial port
        self.serial_port = Serial('COM29', 115200, dsrdtr=True)

        # Initiate Serial Thread
        self.serialThread = SerialThread(self.serial_port)
        self._thread = QThread()
        self.serialThread.moveToThread(self._thread)

        self.serialThread.connectionSuccess.connect(self.connection_success)
        self.serialThread.connectionFailed.connect(self.connection_failed)
        self.serialThread.readFailed.connect(self.error_on_read)

        self._thread.started.connect(self.serialThread.run)

        self.allData = ''

        self.outputBox = self.findChild(QTextEdit, 'outputBox')
        self.serialThread.dataReceived.connect(self.updateOutputBox)

        # setup graphs
        self.altitudeGraph = TelemetryGraph(self.findChild(PlotWidget, 'altitudeGraph'))
        self.altitudeGraph.setTitle('Altitude')
        self.altitudeGraph.addLine()

        self.tempGraph = TelemetryGraph(self.findChild(PlotWidget, 'tempGraph'))
        self.tempGraph.setTitle('Temperature')
        self.tempGraph.addLine()

        self.accelGraph = TelemetryGraph(self.findChild(PlotWidget, 'accelGraph'), legend=True)
        self.accelGraph.setTitle('Acceleration')
        self.accelGraph.addLine('x', 'red')
        self.accelGraph.addLine('y', 'green')
        self.accelGraph.addLine('z', 'blue')

        self.gyroGraph = TelemetryGraph(self.findChild(PlotWidget, 'gyroGraph'), legend=True)
        self.gyroGraph.setTitle('Gyro')
        self.gyroGraph.addLine('x', 'red')
        self.gyroGraph.addLine('y', 'green')
        self.gyroGraph.addLine('z', 'blue')

        self.y = 0

        self._thread.start()  # do this last!!!! this will make the serial port start reading

    @QtCore.pyqtSlot()
    def connection_success(self):
        print('Connected!')

    @QtCore.pyqtSlot(str)
    def connection_failed(self, error):
        print(error)

    @QtCore.pyqtSlot(str)
    def error_on_read(self, error):
        print(error)

    @QtCore.pyqtSlot(bytes)
    def updateOutputBox(self, data):
        try:
            self.allData += unicode(data, errors='ignore')

            if self.allData.find('START') != -1 and self.allData.find('END') != -1:
                s = self.allData.find('START')
                e = self.allData.find('END')

                data = self.allData[s + 5:e + 3].split(',')
                self.allData = self.allData[e + 3:]

                telemetry = 'Altitude: %s\nTemperature: %s\n'\
                            'Accel X: %s\nAccel Y: %s\nAccel Z: %s\n'\
                            'Gyro X: %s\nGyro Y: %s\nGyro Z: %s\n\n'\
                            % (data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])

                self.outputBox.insertPlainText(telemetry)
                self.outputBox.ensureCursorVisible()

                self.y += 1

                self.altitudeGraph.plotData(float(data[1]), self.y)
                self.tempGraph.plotData(float(data[2]), self.y)

                self.accelGraph.plotData(float(data[3]), self.y, name='x')
                self.accelGraph.plotData(float(data[4]), self.y, name='y')
                self.accelGraph.plotData(float(data[5]), self.y, name='z')

                self.gyroGraph.plotData(float(data[6]), self.y, name='x')
                self.gyroGraph.plotData(float(data[7]), self.y, name='y')
                self.gyroGraph.plotData(float(data[8]), self.y, name='z')

        except Exception as e:
            print(str(e))

    def closeEvent(self, event):
        self.serialThread.stop()
        self._thread.quit()
        self._thread.wait()


app = QApplication([])
window = UI()
window.show()
app.exec()