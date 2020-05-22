from django.urls import path
from .views import SignUpView,SignInView

urlpatterns = [
	path('/signup', SignUpView.as_view()),
	path('/signin', SignInView.as_view())
	# name signup method as accountView so that we can use 2 http method: GET, POST, which can be used as signing up and looking up our account at one time (more economical) *include as many http methods per class
]
