from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.views import LoginView
from django.shortcuts import render
#for login view
def UserRegister(request):
    context = {
        'some_variable': 'some_value',
    }
    return render(request, 'register.html', context)
# Class based view to Get User Details using Token Authentication
class GetDeatils(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class UserRegister(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
  
  
