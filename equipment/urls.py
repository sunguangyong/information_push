from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [

    url(r'^device/', include("equipment.device.urls")),
    url(r'^authentication/', include("equipment.authentication.urls")),
    url(r'^commandy/', include("equipment.commandy.urls")),
]