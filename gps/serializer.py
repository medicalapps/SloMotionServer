from datetime import datetime
from rest_framework.serializers import ModelSerializer, SerializerMethodField, HyperlinkedModelSerializer
from gps.models import GPSDataPoint, Route


class GPSDataPointSerializer(ModelSerializer):

    class Meta:
        model = GPSDataPoint
        fields = "__all__"


class GPSRouteSerializer(ModelSerializer):

    class Meta:
        model = Route
        fields = "__all__"