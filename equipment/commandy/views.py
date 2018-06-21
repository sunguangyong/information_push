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


class Commandys(APIView):
	# 命令下发
	def post(self,request):
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
		print 666666666666666666666,params


		print 444444444444444444444444444444444444444,device_id	
		print 555555555555555555555555,CONF['url']['commandys']
		response = requests.post(url=CONF['url']['commandys'], data=params, cert=CONF['cert'],
						  headers=headers, verify=False)
		print 77777777777777777777,response.text
		return HttpResponse(content=response.text)







