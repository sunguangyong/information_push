from django.conf.urls import url
from django.contrib import admin
from views import Commandys

urlpatterns = [
    url(r'^info/', Commandys.as_view()),
]
