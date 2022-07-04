from datetime import datetime
from rest_framework.serializers import ModelSerializer, SerializerMethodField, HyperlinkedModelSerializer
from gps.models import GPSDataPoint


class GPSDataPointSerializer(ModelSerializer):

    class Meta:
        model = GPSDataPoint
        fields = "__all__"


