from django.conf.urls import url
from django.contrib import admin
from auth_views import Auth
from refresh_token_views import Refresh

urlpatterns = [
    url(r'^auth/', Auth.as_view()),
    url(r'^refresh/', Refresh.as_view()),
]
