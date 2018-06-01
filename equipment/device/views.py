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

class Device(APIView):

	# 注册直连设备
	def post(self,request):
		Token = "Bearer " + request.GET.get("Token")
		headers = {'Content-Type': 'application/json', "Authorization": Token,
				   "app_key": request.GET.get("app_id")}
		params = request.body
		response = requests.post(url="https://180.101.147.89:8743/iocm/app/reg/v1.2.0/devices", data=params, cert=CERT,
						 headers=headers, verify=False)
		return HttpResponse(content=response.text)

	# 查询设备状态
	def get(self,request):  # ok
		Token =  "Bearer " + request.GET.get("Token")
		headers = {'Content-Type': 'application/json', "Authorization": Token,
				   "app_key": request.GET.get("app_id")}

		response = requests.get(
			url="https://180.101.147.89:8743/iocm/app/reg/v1.1.0/devices/%s"%(request.GET['device_id']),
			cert=CERT, headers=headers, verify=False)
		return HttpResponse(content=response.text)

	# 修改设备信息
	def put(self,request):
		Token = "Bearer " + request.GET.get("Token")
		headers = {'Content-Type': 'application/json', "Authorization": Token,
				   "app_key": request.GET.get("app_id")}
		name = json.loads(request.body).get('name')
		device_id = request.GET.get('device_id')
		params = {
			"name": name
		}
		params = json.dumps(params)
		response = requests.put(url = "https://180.101.147.89:8743/iocm/app/dm/v1.2.0/devices/%s"%device_id, data=params, cert=CERT,
								headers=headers, verify=False)
		url = "https://180.101.147.89:8743/iocm/app/dm/v1.2.0/devices/47914f6b-075c-419e-a5bb-2e87fc753663"
		return HttpResponse(response.text)

	# 删除设备
	def delete(self, request): # TODO postman未实现
		Token = "Bearer " + request.GET.get("Token")
		headers = {'Content-Type': 'application/json', "Authorization": Token,
				   "app_key": request.GET.get("app_id")}
		device_id = request.GET.get("device_id")
		response = requests.delete(url="https://180.101.147.89:8743/iocm/app/dm/v1.1.0/devices/%s"%device_id, cert=CERT,
								headers=headers, verify=False)
		return HttpResponse(response.text)





