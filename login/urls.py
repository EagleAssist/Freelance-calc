from django.urls import path
from .views import UserRegistrationView, UserLoginView
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('',TemplateView.as_view(template_name='basic.html'))
    # Add other views/URLs as needed
]