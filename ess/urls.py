"""
URL configuration for ess project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to ESS Project!")


urlpatterns = [
    path('', home_view, name='home'),
    path('auth/', include('authentication.urls')),
    path('att/', include('attendance.urls')),
    path('leave/', include('leaves.urls')),
    path('chat/', include('chat.urls')),
    path('kpi/', include('kpi.urls')),
    path('pay/', include('payroll.urls')),
    path('docs/', include('documents.urls')),  
    path('pro/', include('projectmanagement.urls')), 
]
