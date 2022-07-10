from datetime import timedelta
import sys
 

import os

import io
from time import time
 
import pynmea2
import serial
import serial.tools.list_ports
from gps.models import GPSDataPoint, GPSSettings, Route 

import geopy.distance 
import math, numpy as np


 
class GPSReader():
    
    def __init__(self):
        try:
            super().__init__()

            availableports = list(serial.tools.list_ports.comports())
            for port in availableports:
                print(port)

            if os.name == 'nt':
                self.ser = serial.Serial('COM16',baudrate=4800,timeout=1)
            
            else:

                self.ser = serial.Serial('/dev/ttyUSB0',baudrate=4800,timeout=1)
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
        while 1:
            try:
                iterator = 0
                iterator += 1 
                if iterator > 80:
                    iterator = 0   
                msg = "No incoming line..."
            
                try:
                    line = self.sio.readline()
                    #print(line)
                    parsedline = pynmea2.parse(line)
                
                except Exception as e:
                    print ('pynmea-error: ' ,e)
                    continue

                
                deciLat = parsedline.latitude 
                decilng = parsedline.longitude
                print(deciLat, decilng)
                if deciLat > 0 and decilng >0:

                    
                    newGPSPointe = GPSDataPoint.objects.create(
                        lat = deciLat,
                        lng = decilng
        
                    )

                
                AllPioints = GPSDataPoint.objects.filter(useForCalculation = True)
                LenAllPoints = len(AllPioints) 
                settings = GPSSettings.objects.all().first()
                trace = settings.traceLeanght
                if LenAllPoints < trace -1:
                    trace = LenAllPoints - 1
                calcfrompoint = LenAllPoints - trace
                calcFrom = AllPioints[calcfrompoint]
                newGPSPointe = AllPioints.last()
                timediff =  (newGPSPointe.timestamp - calcFrom.timestamp).seconds
                bearing, distanse = self.getbearingAndSpeed(calcFrom.lat, calcFrom.lng, newGPSPointe.lat, newGPSPointe.lng)

                newGPSPointe.bearing = bearing


                newGPSPointe.velocity = (distanse)/timediff    



                print(f'writing new GPS-point: lat:{newGPSPointe.lat} lng:{newGPSPointe.lng} speed:{newGPSPointe.velocity} bearing:{newGPSPointe.bearing}')
                
                # else:

                #     continue

            except Exception as e:
                print('Generall Error: ', (e))    
            
    
    def getbearingAndSpeed(self, lat1,lon1,lat2,lon2):
        bearing = -1
        distanse = -1
    
        try:
            distanse = geopy.distance.geodesic((lat1,lon1), (lat2,lon2)).m
        except:
            pass
    
        try:

            dLon = lon2 - lon1;
            y = math.sin(dLon) * math.cos(lat2);
            x = math.cos(lat1)*math.sin(lat2) - math.sin(lat1)*math.cos(lat2)*math.cos(dLon);
            bearing = np.rad2deg(math.atan2(y, x));
            if bearing < 0: bearing+= 360
        except:
            pass

        return [bearing, distanse]


    def navigate(self):
        ActiveRoutes = Route.objects.filter(active=True)
        if len(ActiveRoutes) == 1:
            ActiveRoute = ActiveRoutes[0]
            remainingWaypoints = ActiveRoute.waypoints.filter(visited=False).order_by('order')
        elif len(ActiveRoutes) > 1:
            
#gpsReader = GPSReader()
