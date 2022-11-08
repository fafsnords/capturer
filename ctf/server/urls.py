from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('challenge/', views.challenge, name='challenge'),
    path('challenge/settings/', views.settings, name='settings'),
    path('challenge/flag/', views.flag, name='flag'),
    path('solvers/', views.solvers, name='solvers'),
    path('challenge/log_out/', views.log_out, name='log_out')
]