"""ctf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('server.urls')),
    path('about/', include('server.urls')),
    path('sign_up/', include('server.urls')),
    path('sign_in/', include('server.urls')),
    path('challenge/', include('server.urls')),
    path('challenge/settings/', include('server.urls')),
    path('challenge/flag/', include('server.urls')),
    path('solvers/', include('server.urls')),
    path('challenge/log_out/', include('server.urls'))
]
