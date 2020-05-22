import json
from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import Users
from django.shortcuts import render
from django.db import IntegrityError
import bcrypt
import jwt
from my_settings import SECRET

class SignUpView(View):
	def post(self,request):
		try:
			data = json.loads(request.body)
			password = bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt())
			crypted = password.decode('utf-8')
			Users.objects.create(
				username = data['username'],
				email= data['email'],
				password= crypted)
			return HttpResponse(status=200)
		except KeyError:
			return JsonResponse({'message':'FAILED'},status=400)
		except IntegrityError:
			return JsonResponse({'message':'DUPLICATE_EMAIL_ENTRIES'},status=400)

class SignInView(View):
	def post(self,request):
		try:
			data = json.loads(request.body)
			if Users.objects.filter(email=data['email']).exists():
				user = Users.objects.get(email=data['email'])
				if bcrypt.checkpw(data['password'].encode('utf-8'),user.password.encode('utf-8')):
					token = jwt.encode({'email':data['email']},SECRET,algorithm='HS256')
					token = token.decode('utf-8') 

					return JsonResponse({'token':token}, status=200)
				else:
					return JsonResponse({'message':'INVALID_PASSWORD'})
			else:
				return JsonResponse({'message':'INVALID_USER'}, status=400)
		except KeyError:
			return JsonResponse({'message':'INVALID_KEY'}, status=400)	
				

class TokenCheckView(View):
	def post(self,request):
		data = json.laods(request.body)
		user_token = jwt.decode(data['token'],SECRET,algorithm='HS256')
		if Users.objects.filter(email=user_token['email']).exists():
			return HttpResponse(status = 200)
		return HttpResponse(status = 400)
