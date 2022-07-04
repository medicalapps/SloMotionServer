from turtle import speed
from django.db import models

# Create your models here.

class GPSDataPoint(models.Model):
    lat = models.FloatField(blank=True, default=0.0)
    lng = models.FloatField(blank=True, default=0.0)
    bearing = models.IntegerField(blank=True, default=0)
    velocity = models.FloatField(blank=True, default=0.0)
    timestamp = models.DateTimeField(auto_now=True)
    
    