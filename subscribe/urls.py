from django.conf.urls import url
from django.contrib import admin
from views import SubscribeInfo

urlpatterns = [
    url(r'^info/', SubscribeInfo.as_view()),
]

