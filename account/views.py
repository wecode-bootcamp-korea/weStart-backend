import json
import bcrypt
import jwt

from django.views import View
from django.http import HttpResponse, JsonResponse


from .models import Account
from westagram_project.settings import SECRET_KEY

class SignUpView(View):
    def post(self, request):
        signup_data = json.loads(request.body)

        try:
            if Account.objects.filter(email=signup_data['email']).exists():
                return HttpResponse(status=401)

            ## encryption below

            password = signup_data['password'].encode('utf-8')

            password_encrypt = bcrypt.hashpw(password, bcrypt.gensalt())
            password_encrypt = password_encrypt.decode('utf-8')
            
            Account(
                email = signup_data['email'],
                username = signup_data['username'],
                password = password_encrypt
            ).save()

            return HttpResponse(status=200)

        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status=400)


class SignInView(View):
    def post(self, request):
        signin_data = json.loads(request.body)

        try:
            if Account.objects.filter(email=signin_data['email']).exists():
                user = Account.objects.get(email=signin_data['email'])
        
                ## check password from db

                if bcrypt.checkpw(signin_data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    token = jwt.encode({'email':signin_data['email']}, SECRET_KEY, algorithm = "HS256")
                    token = token.decode('utf-8')

                    return JsonResponse({"token":token}, status=200)

                else:
                    return HttpResponse(status=401)

            return HttpResponse(status=400)
        
        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status=400)

class TokenCheckView(View):
    def post(self, request):
        data = json.loads(request.body)

        token_info = jwt.decode(data['token'], SECRET_KEY, algorithm = 'HS256')

        if Account.objects.filter(email=token_info['email']).exists():
            return HttpResponse(status=200)
        
        return HttpResponse(status=403)


