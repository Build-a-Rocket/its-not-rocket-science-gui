from os import system
import random

from PyQt6 import QtCore, uic
from PyQt6.QtCore import QThread, pyqtSignal, QObject
from PyQt6.QtWidgets import QApplication, QTextEdit, QWidget, QLabel
from PyQt6.QtGui import QPixmap
from pyqtgraph import PlotWidget
from PyQt6 import *
#from PySide6.QtWidgets import QLabel
import pyqtgraph
from serial import Serial, unicode
from PIL import Image
import io
class TelemetryGraph:

    def __init__(self, graph, legend=False):
        self._graph = graph
        self._graph.setBackground('w')

        self.styles = {'color': '#000000', 'font-size': '12px'}

        self.y_limit = 30

        self._x = dict()
        self._y = dict()
        self._lines = dict()
        self._pen = dict()

        if legend:
            self._graph.addLegend(offset=(0, 0))

    def addLine(self, name='default', color='black'):
        self._x[name] = [0]
        self._y[name] = [0]
        self._pen[name] = pyqtgraph.mkPen(color=color)
        self._lines[name] = self._graph.plot(self._x[name], self._y[name], name=name)

    def plotData(self, x, y, name='default'):
        self._x[name].append(x)
        self._y[name].append(y)

        self._x[name] = self._x[name][-1*(self.y_limit):]
        self._y[name] = self._y[name][-1*(self.y_limit):]
        # if len(self._x[name]) > self.y_limit:
        #     self._x[name] = self._x[name][1:]
        #     self._y[name] = self._y[name][1:]

        self._lines[name].setData(self._y[name], self._x[name], name=name, pen=self._pen[name])

    def setBackgroundColor(self, color='w'):
        self._graph.setBackground(color)

    def setTitle(self, name, color='black'):
        self._graph.setTitle(name, color=color, size='12pt')

    def setYLabel(self, name):
        self._graph.setLabel('left', name, **self.styles)

    def setXLabel(self, name):
        self._graph.setLabel('bottom', name, **self.styles)
class SerialThread(QObject):

    connectionFailed = pyqtSignal(str)
    connectionSuccess = pyqtSignal()
    readFailed = pyqtSignal(str)
    dataReceived = pyqtSignal(bytes)

    def __init__(self, serial_instance):
        """\
        Initialize thread.
        Note that the serial_instance' timeout is set to one second!
        Other settings are not changed.
        """
        QObject.__init__(self)
        self.serial = serial_instance
        self.serial.close()
        self.alive = True

    def stop(self):
        """Stop the reader thread"""
        self.alive = False
        if hasattr(self.serial, 'cancel_read'):
            self.serial.cancel_read()

        self.serial.close()

    def run(self):

        if not hasattr(self.serial, 'cancel_read'):
            self.serial.timeout = 1

        try:
            self.serial.open()
        except Exception as e:
            self.alive = False
            self.connectionFailed.emit(str(e))
            return
        error = None
        self.connectionSuccess.emit()

        while self.alive and self.serial.is_open:
            try:
                # read all that is there or wait for one byte (blocking)
                data = self.serial.read(self.serial.in_waiting or 1)
            except serial.SerialException as e:
                # probably some I/O problem such as disconnected USB serial
                # adapters -> exit
                error = e
                self.readFailed.emit(str(e))
                break
            else:
                if data:
                    # make a separated try-except for called user code
                    try:
                        self.dataReceived.emit(data)
                    except Exception as e:
                        error = e
                        self.readFailed.emit(str(e))
                        break
        self.alive = False
        self.connectionFailed.emit()
class bytesImage:
    def __init__(self, image, initial_image_binary):
        print(image)
        self.image = image
        self.__update__(initial_image_binary) 
        
        
    def __update__(self, binary):
        self.image.setPixmap(binary)
        self.image.show()
        
class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()
        
        # Load the UI File
        uic.loadUi("GUI/design4.ui", self)
        
        #Connect to the Serial Port
        self.__connectSerial__("COM6")
        
        # update the Text Box
        self.__updateRAW__()

        # Init the graphs
        self.__setupPlots__()
        
        # Init image
        self.__setupImage__()
        
        # show the app
        self.y = 0
        self.show()
        self._thread.start()
        
    def __connectSerial__(self, port):
        self.serial_port = Serial(port)
        
        
        self.serialThread = SerialThread(self.serial_port)
        self._thread = QThread()
        self.serialThread.moveToThread(self._thread)
        
        self.serialThread.connectionSuccess.connect(self.connection_success)
        self.serialThread.connectionFailed.connect(self.connection_failed)
        self.serialThread.readFailed.connect(self.error_on_read)
        
        self._thread.started.connect(self.serialThread.run)

    def __updateRAW__(self):
        self.allData = ''
        self.outputBox = self.findChild(QTextEdit, 'RAW')
        self.serialThread.dataReceived.connect(self.update)
        
    def __setupPlots__(self):
        # setup graphs
        self.altitudeGraph = TelemetryGraph(self.findChild(PlotWidget, 'ALTITUDE'))
        self.altitudeGraph.setTitle('Altitude')
        self.altitudeGraph.addLine()

        self.tempGraph = TelemetryGraph(self.findChild(PlotWidget, 'TEMPERATURE'))
        self.tempGraph.setTitle('Temperature')
        self.tempGraph.addLine()

        self.accelGraph = TelemetryGraph(self.findChild(PlotWidget, 'ACCELERATION'), legend=True)
        self.accelGraph.setTitle('Acceleration')
        self.accelGraph.addLine('x', 'red')
        self.accelGraph.addLine('y', 'green')
        self.accelGraph.addLine('z', 'blue')

        self.gyroGraph = TelemetryGraph(self.findChild(PlotWidget, 'GYRO'), legend=True)
        self.gyroGraph.setTitle('Gyro')
        self.gyroGraph.addLine('x', 'red')
        self.gyroGraph.addLine('y', 'green')
        self.gyroGraph.addLine('z', 'blue')
    
    def __setupImage__(self):
        self.image = bytesImage(self.findChild(QLabel, 'VIDEO'), QPixmap("GUI\StarterImage.jpg"))
    
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
    def update(self, data):
        self.plotserialupdate(data)

    def plotserialupdate(self, data):
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
            # check if the data starts with VED and ends with VFM
            # if ("VFM" in self.allData) and ("VED" in self.allData):
            #         imadata = self.allData
            #         start_index = imadata.find('VFM') # Find index of start sequence
            #         end_index = imadata.find('VED')
            #         imadata = imadata[start_index + 3 : end_index ] # Slice out bytes between start and end sequences
            #         print(imadata)
            #         f = open("log.txt", "w")
            #         f.write(imadata)
            #         f.close()
            #         imadata = bytes(imadata, "UTF-8")
                    
            #         # Convert imdata to an image using PIL

            #         image = Image.open(io.BytesIO(imadata)) # Open data as a file-like object using BytesIO
            #         self.allData = self.allData[end_index + 3:]
            
            if ("VED" in self.allData) and ("VFM" in self.allData):
                s = self.allData.find('VED')
                e = self.allData.find('VFM')
                #print(e, s)
                data = self.allData[e + 3: s]
                data = bytes(data, "utf-8")
                print(data)
                image = Image.frombytes("RGB", (239, 175), data)
                pixmap = QPixmap.fromImage(image)
                self.image.__update__(pixmap)
                self.allData = ""
                print(self.allData)
            
        
            
        except Exception as e:
            print(str(e))
    
    

# initialize the app
app = QApplication([])
window = UI()
window.show()
app.exec()