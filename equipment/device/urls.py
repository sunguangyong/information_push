from django.conf.urls import url
from django.contrib import admin
from views import Device

urlpatterns = [
    url(r'^info/', Device.as_view()),
]
