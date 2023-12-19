from django.urls import path,include
from .views import UserRegister, GetDeatils,UserRegister
urlpatterns = [
  path('user_register/', UserRegister.as_view()),

  path('getdetails/',GetDeatils.as_view()),
  path('register/',UserRegister.as_view()),
]
