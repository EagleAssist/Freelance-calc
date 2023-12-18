from django.urls import path,include
from .views import UserRegister, GetDeatils
urlpatterns = [
  path('getdetails/',GetDeatils.as_view()),
  path('register/',UserRegister.as_view()),
]
