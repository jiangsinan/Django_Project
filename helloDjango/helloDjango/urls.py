"""helloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import path, include


def index(request: HttpRequest):
    users = [
        {'id': 1, 'name': 'jsn'},
        {'id': 2, 'name': 'jack'},
        {'id': 3, 'name': 'tom'},
    ]
    return render(request, 'index.html', {'users': users, 'msg': '所有用户'})


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('index', index),
                  path('user/', include('mainapp.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
