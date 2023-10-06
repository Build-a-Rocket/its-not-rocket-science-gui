import time
import serial
serialPort = "COM30"

ser = serial.Serial(serialPort)
print("codeing")
buffer = ""
seperatorFound = False
seperator = bytes("~", "utf-8")
while True:
    if ser.in_waiting > 0:
        payload = ser.read()
        #print("data received")
        #print(payload)
        if (payload == seperator) and (seperatorFound == False):
            seperatorFound = True
            continue
            
        
        if seperatorFound == True:
            if payload == seperator:
                seperatorFound = False
                print(f"buffer = {buffer}")
                buffer = ""
                continue
            else:
                buffer += payload.decode("utf-8")
                continue
    
                
                