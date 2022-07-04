from django.urls import path
from gps.views import CurrentLocation

urlpatterns = [
    path('getlocation', CurrentLocation.as_view()),
]