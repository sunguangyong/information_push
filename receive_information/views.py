from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView

# Create your views here.
class Test(APIView):
	def get(self,request):
		print 'hello'
		# return render(request,{"file_id":601, "info_company":{"company_id":"123456"}})
		return HttpResponse(content='{"file_id":601, "info_company":{"company_id":"123456"}}',status=200,content_type="application/json")

	def post(self,request):
		return HttpResponse(content=request.body,status=200,content_type="application/json")



