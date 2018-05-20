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

CERT = ("/etc/nginx/cert/client.crt", "/etc/nginx/cert/client.key")


class Refresh(APIView):
	# 刷新Tokne ?
	def post(self, request):
		app_id = json.loads(request.body).get("app_id")
		passwd = json.loads(request.body).get("secret")
		refreshToken = json.loads(request.body).get("refreshtoken")
		headers = {'Content-Type': 'application/json'}
		params = {}
		params["appId"] = app_id
		params["secret"] = passwd
		params["refreshToken"] = refreshToken
		cert = ("/etc/nginx/cert/client.crt", "/etc/nginx/cert/client.key")
		response = requests.post(url="https://180.101.147.89:8743/iocm/app/sec/v1.1.0/refreshToken", data=params, cert=CERT,
						  verify=False, headers=headers)
		return HttpResponse(content=response.text)





