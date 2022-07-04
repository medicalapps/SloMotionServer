from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from gps.models import GPSDataPoint
from gps.serializer import GPSDataPointSerializer


class CurrentLocation(APIView):
    """Return companies within Medtanken Group with belonging units"""
    queryset = GPSDataPoint.objects.all()
    serializer_class = GPSDataPointSerializer
 
    def get(self, request):
        data = self.queryset.last()
        data2 = GPSDataPointSerializer(data).data
        return Response(data2, status=status.HTTP_200_OK)