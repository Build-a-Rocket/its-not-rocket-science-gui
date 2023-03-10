from tkinter import *
from random import randint
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.backends.backend_tkagg as tkagg
import tkinter as Tk
import numpy as np
import serial
import matplotlib.animation as animation
class matplotGraph:
    """This a a class that takes care of making a graph and updating it with the relative data
    """    
    def __init__(self, points):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.points = points
        self.ani = 0
        
        # plt.title(str(i))
            
        
        
    def update(self, time, data):

        self.ax.clear()
        for i in data:
            self.ax.plot(time, i)
        
        print("update plot")
        self.show()
    
    def show(self):
        self.fig.show()
        # animation.FuncAnimation(self.fig, self.update, fargs=(xs, ys), interval=1000)
        plt.draw()
        plt.pause(0.1)







# layout = [
#         [],
#         [sg.Submit(), sg.Cancel()]
#          ]

#window = sg.Window("Demo", layout)
serialPort = "COM30"
ser = serial.Serial(serialPort)
buffer = ""
seperatorFound = False
seperator = bytes("~", "utf-8")

accelerationGraph = matplotGraph(1)
dataNum = (30 * -1)
#otherGraph = matplotGraph()
time = []
altitude = []
temp = []
gx = []
gy = []
gz = []
ax = []
ay = []
az = []

while True:
    # event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    



    if ser.in_waiting > 0:
        payload = ser.read()
        #print("data received")
        #print(payload)
        if (payload == seperator) and (seperatorFound == False):
            seperatorFound = True
            # accelerationGraph.show()
            # otherGraph.show()
            continue
            
        
        if seperatorFound == True:
            if payload == seperator:
                seperatorFound = False
                print(f"buffer = {buffer}")
                if buffer == "":
                    buffer = ""
                    print("buffer was empty")
                    continue
                data = buffer.split(",")
                for i in range(len(data)):
                    data[i] = float(data[i])
                # all logic for updating goes here
                time.append(data[0])
                altitude.append(data[1])
                temp.append(data[2])
                gx.append(data[3])
                gy.append(data[4])
                gz.append(data[5])
                ax.append(data[6])
                ay.append(data[7])
                az.append(data[8])
                
                time = time[dataNum:]
                altitude = altitude[dataNum:]
                temp = temp[dataNum:]
                gx = gx[dataNum:]
                gy = gy[dataNum:]
                gz = gz[dataNum:]
                ax = ax[dataNum:]
                ay = ay[dataNum:]
                az = az[dataNum:]
                
                
                
                accelerationGraph.update(time, [ax, ay, az])
                
                
                
                
                
                buffer = ""
                
                
                continue
            else:
                buffer += payload.decode("utf-8")
                continue
        
    # if event == "OK" or event == sg.WIN_CLOSED:
    #     break

#window.close()