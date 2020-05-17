import json
from django.views import View
from django.http import JsonResponse
from .models import Comment
from django.shortcuts import render

class CommentView(View):
        def post(self,request):
                try:
                        data = json.loads(request.body)
                        Comment.objects.create(email= data['email'],comment= data['comment'])
                        return JsonResponse({'message':'SUCCESS'},status=200)
                except KeyError:
                        return JsonResponse({'message':'FAILED'},status=400)
# Create your views here.
