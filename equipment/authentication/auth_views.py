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
CERT = ("/etc/nginx/cert/client.crt", "/etc/nginx/cert/client.key")

class Auth(APIView):

	# 鉴权
	def post(self,request):
		app_id = json.loads(request.body).get("app_id")
		passwd = json.loads(request.body).get("secret")
		headers = {'Content-Type': 'application/x-www-form-urlencoded'}
		params = {}
		params["appId"] = app_id
		params["secret"] = passwd
		response = requests.post(url=CONF['url']['auth'], data=params, cert=CONF['cert'],
						  verify=False, headers=headers)
		return HttpResponse(content=response.text)





