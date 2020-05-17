import json
from django.views import View
from django.http import JsonResponse
from .models import Users
from django.shortcuts import render

class SignUpView(View):
	def post(self,request):
		try:
			data = json.loads(request.body)
			Users.objects.create(email= data['email'],password= data['password'])
			return JsonResponse({'message':'SUCCESS'},status=200)
		except KeyError:
			return JsonResponse({'message':'FAILED'},status=400)

class SignInView(View):
	def post(self,request):
		try:
			data = json.loads(request.body)
			if data['email'] and data['password']:
				return JsonResponse({'message':'SUCCESS'}, status=200)
		except KeyError:
			return JsonResponse({'message':'FAILED'}, status=400)	
				


# Create your views here.
