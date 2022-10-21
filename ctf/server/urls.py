from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('challenge/', views.challenge, name='challenge'),
    path('challenge/flag/', views.flag, name='flag'),
    path('hall_of_fame/', views.hall_of_fame, name='hall_of_fame'),
    path('challenge/log_out/', views.log_out, name='log_out')
]