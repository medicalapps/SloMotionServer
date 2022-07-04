import sys
 

 

import io
from time import time
 
import pynmea2
import serial
import serial.tools.list_ports
from gps.models import GPSDataPoint 

 


 

 
 
class GPSReader():
    
    def __init__(self):
        try:
            super().__init__()

            availableports = list(serial.tools.list_ports.comports())
            for port in availableports:
                print(port)


            self.ser = serial.Serial('COM3',baudrate=4800,timeout=1)
            self.sio = io.TextIOWrapper(io.BufferedRWPair(self.ser, self.ser))

            self.readGPSData()
        except Exception as e:
            print(e)
    def ReInit(self):
    
        availableports = list(serial.tools.list_ports.comports())
        for port in availableports:
            print(port)


        self.ser = serial.Serial('/dev/ttyUSB0',baudrate=4800,timeout=1)
        self.sio = io.TextIOWrapper(io.BufferedRWPair(self.ser, self.ser))

        self.readGPSData()
        
    def readGPSData(self):
        
        iterator = 0
        while 1:
            iterator += 1 
            if iterator > 80:
                iterator = 0   
            msg = "No incoming line..."
        
            try:
                line = self.sio.readline()
                #print(line)
                parsedline = pynmea2.parse(line)
                #print(parsedline)
                msg = repr(parsedline)
            except serial.SerialException as e:
                msg = 'Device error: {}'.format(e)        
            except pynmea2.ParseError as e:
                msg = 'Parse error: {}'.format(e)
            except Exception as e:
                msg = 'Generell error: {}'.format(e)
            
            
            newGPSPointe = GPSDataPoint.objects.create(
                lat = 10.2 + iterator,
                lng = 20.3 + iterator,
                bearing = iterator,
                velocity = 10 + (iterator*0.1)
    
            )
            
            print('writing new GPS-point: ', newGPSPointe)
            
    
   
 

#gpsReader = GPSReader()
