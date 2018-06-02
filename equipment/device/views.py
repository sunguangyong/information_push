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
class Device(APIView):

	# 注册直连设备
	def post(self,request):
		Token = "Bearer " + request.GET.get("Token")
		headers = {'Content-Type': 'application/json', "Authorization": Token,
				   "app_key": request.GET.get("app_id")}
		params = request.body
		response = requests.post(url=CONF['url']['devicepost'], data=params, cert=CONF['cert'],
						 headers=headers, verify=False)
		print response
		return HttpResponse(content=response.text)

	# 查询设备状态
	def get(self,request):  # TODO
		Token =  "Bearer " + request.GET.get("Token")
		headers = {'Content-Type': 'application/json', "Authorization": Token,
				   "app_key": request.GET.get("app_id")}

		response = requests.get(
			url=CONF['url']['deviceget']+request.GET['device_id'],
			cert=CONF['cert'], headers=headers, verify=False)
		return HttpResponse(content=response.text)

	# 修改设备信息
	def put(self,request):
		Token = "Bearer " + request.GET.get("Token")
		headers = {'Content-Type': 'application/json', "Authorization": Token,
				   "app_key": request.GET.get("app_id")}
		device_id = request.GET.get('device_id')
		params = request.body
		response = requests.put(url = CONF['url']['deviceput']+device_id, data=params, cert=CONF['cert'],
								headers=headers, verify=False)
		#url = "https://device.api.ct10649.com:8743/iocm/app/dm/v1.2.0/devices/47914f6b-075c-419e-a5bb-2e87fc753663"
		return HttpResponse(response.text)

	# 删除设备
	def delete(self, request):  
		Token = "Bearer " + request.GET.get("Token")
		headers = {'Content-Type': 'application/json', "Authorization": Token,
				   "app_key": request.GET.get("app_id")}
		device_id = request.GET.get("device_id")
		response = requests.delete(url=CONF['url']['devicedelete']+device_id, cert=CONF['cert'],
								headers=headers, verify=False)
		return HttpResponse(response.text)





