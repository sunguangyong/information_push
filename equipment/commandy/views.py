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

class Commandys(APIView):
	# 命令下发
	def post(self,request):
		# app_id = json.loads(request.body).get("app_id")
		# token = json.loads(request.body).get("token")
		app_id = request.GET.get("app_id")
		token = "Bearer " + request.GET.get("Token")
		device_id = request.GET.get("device_id")
		headers = {'Content-Type': 'application/json', "Authorization": token, "app_key": app_id}
		command = json.loads(request.body).get("command")
		params = {
			"deviceId": device_id,
			"command": {
				"serviceId": "ReportData",
				"method": "SET_PRESSURE_READ_PERIOD",
				"paras": {
					"value": command
				}
			}, "expireTime": 0
		}
		params = json.dumps(params)
		response = requests.post(url="https://device.api.ct10649.com:8743/iocm/app/cmd/v1.4.0/deviceCommands", data=params, cert=CERT,
						  headers=headers, verify=False)
		return HttpResponse(content=response.text)







