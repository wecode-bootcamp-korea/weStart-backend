import jwt
import json
import requests

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from my_settings import SECRET
from account.models import Users

def login_decorator(func):
	def wrapper(self,request,*args,**kwargs):
		access_token = request.headers.get('Authorization',None)
		if access_token:
			try:
				print("SECRET=",end=""), print(SECRET)
				print("access_token=",end=""), print(access_token)
				payload = jwt.decode(access_token, SECRET, algorithm='HS256')
				print("payload=",end=""), print(payload)
				user = Users.objects.get(email=payload['email'])
				request.user = user
			except KeyError:
				return HttpResponse(status=400)

			except jwt.exceptions.DecodeError:
				return JsonResponse({'message':'INVALID_TOKEN'},status=400)

			except Users.DoesNotExist:
				return JsonResponse({'message':'INVALID_USER'},status=400)

			return func(self,request,*args, **kwargs)
		else:
			return JsonResponse({'message':'NEED_LOGIN'},status=401)
	return wrapper
