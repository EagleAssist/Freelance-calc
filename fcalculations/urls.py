from django.urls import path
from .views import CalculateView,history,logout_view
from django.views.generic import RedirectView

urlpatterns = [
    path('calculate/', CalculateView.as_view(), name='calculate'),
    path('calculate/history',history.as_view(),name='history'),
    path('calculate/logout',logout_view,name='Logout')
   
   
]