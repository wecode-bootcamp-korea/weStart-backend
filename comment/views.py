import json
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Comment
from account.models import Account

class CommentView(View):
    def post(self, request):
        comment_info = json.loads(request.body)
        username = comment_info['user']
        
        try:
            Comment.objects.create(
                    user = Account.objects.get(username = username),
                    user_comment = comment_info['user_comment'],
            )
            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEY'}, status=400)

    def get(self, request):
        comment_data = list(Comment.objects.values())

        try:
            return JsonResponse({'data':comment_data},status=200)
        except Comment.DoesNotExist:
            return JsonResponse({'message':'COMMENT_DOES_NOT_EXIST'}, status=400)
