from django.urls import path
from .views import CalculateView,history
from django.views.generic import RedirectView

urlpatterns = [
    path('calculate/', CalculateView.as_view(), name='calculate'),
    path('history',history.as_view(),name='history')
    # path('history/<str:username>/', ListView.as_view() , name='Listview')
   
   
]