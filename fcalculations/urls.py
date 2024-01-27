from django.urls import path
from .views import CalculateView,logout_user
from django.views.generic import RedirectView

urlpatterns = [
    path('calculate/', CalculateView.as_view(), name='calculate'),
    # path('logout/', logout_user, name='logout_user'),
    # path('history', views.history, name='history'),
    path('calculate/logout/',RedirectView.as_view(url='login/'))
]