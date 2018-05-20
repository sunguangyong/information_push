from django.conf.urls import url
from django.contrib import admin
from views import Test

urlpatterns = [
    url(r'^info/', Test.as_view()),
]
