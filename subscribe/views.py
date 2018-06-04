# coding:utf-8
import os
import sys
import requests
import urllib3
urllib3.disable_warnings()
import json
from requests.auth import HTTPBasicAuth
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from conf.conf import CONF

class SubscribeInfo(APIView):
    def post(self, request):
	#return HttpResponse(content=request.body)

	Token = "Bearer " + request.GET.get("Token")
	headers = {'Content-Type': 'application/json', "Authorization": Token,
	           "app_key": request.GET.get("app_id")}
	params = request.body
	response = requests.post(url=CONF['url']['subscribeInfo'],
				 data=params, cert=CONF['cert'],headers=headers, verify=False)
	return HttpResponse(content=response.text)

   ''' 
    def get(self,request):
        Token = "Bearer " + request.GET.get("Token")
        headers = {'Content-Type': 'application/json', "Authorization": Token,
                     "app_key": request.GET.get("app_id")}	
        
	response = requests.post(url=CONF['url']['subscribeInfo'],
                                   data=params, cert=CONF['cert'],headers=headers, verify=False)
        return HttpResponse(content=response.text)
   '''



