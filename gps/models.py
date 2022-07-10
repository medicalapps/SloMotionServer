from pyexpat import model
from turtle import speed
from django.db import models

# Create your models here.

class GPSDataPoint(models.Model):
    lat = models.FloatField(blank=True, default=0.0)
    lng = models.FloatField(blank=True, default=0.0)
    bearing = models.IntegerField(blank=True, default=0)
    velocity = models.FloatField(blank=True, default=0.0)
    timestamp = models.DateTimeField(auto_now=True)
    useForCalculation = models.BooleanField(default= True)
    
class GPSWayPoint(models.Model):
    lat = models.FloatField(blank=True, default=0.0)
    lng = models.FloatField(blank=True, default=0.0)
    bearing = models.IntegerField(blank=True, default=0)
    velocity = models.FloatField(blank=True, default=0.0)
    timestamp = models.DateTimeField(auto_now=True)
    useForCalculation = models.BooleanField(default= True)
    order =  models.IntegerField(blank=True, default=-1)
    active = models.BooleanField(default= False)
        
class Route(models.Model):
    name = models.CharField(default='Inget namn', max_length=127)
    timestamp = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default= False)
    waypoints = models.ManyToManyField(GPSWayPoint, default=None)    



class GPSSettings(models.Model):
    traceLeanght = models.IntegerField(blank=True, default=10)


