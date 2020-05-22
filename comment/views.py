import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Comment
from django.shortcuts import render
from account.utils import login_decorator

class CommentView(View):
	@login_decorator
	def post(self,request):
		data = json.loads(request.body)
		Comment.objects.create(
			username = request.user,
			comment= data['comment'])
		return HttpResponse(status=200)

	def get(self,request):
		return JsonResponse({'comment':list(Comment.objects.values())},status=200)
			
		
# Create your views here.
