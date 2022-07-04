from django.contrib import admin
from gps.models import GPSDataPoint

# Register your models here.


@admin.register(GPSDataPoint)
class GPSDataPointAdmin(admin.ModelAdmin):
    search_fields = ["timestamp"]
    pass