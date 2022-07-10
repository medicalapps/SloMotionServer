from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from gps.models import GPSDataPoint, GPSWayPoint, Route
from gps.serializer import GPSDataPointSerializer, GPSRouteSerializer


class CurrentLocation(APIView):
    """Return companies within Medtanken Group with belonging units"""
    queryset = GPSDataPoint.objects.all()
    serializer_class = GPSDataPointSerializer
 
    def get(self, request):
        data = self.queryset.last()
        data2 = GPSDataPointSerializer(data).data
        return Response(data2, status=status.HTTP_200_OK)

class CurrentRoute(APIView):
    """Return companies within Medtanken Group with belonging units"""
    Waypoints = GPSWayPoint.objects.all()
    Routes = Route.objects.all()
    serializer_class = GPSRouteSerializer
 
    def get(self, request):
        data = self.queryset.last()
        data2 = GPSDataPointSerializer(data).data
        return Response(data2, status=status.HTTP_200_OK)

    def post(self, request):
        setActive = request['setActive']
        waypoints = request['wayPoints']



        data = self.queryset.last()
        data2 = GPSDataPointSerializer(data).data
        return Response(data2, status=status.HTTP_200_OK)