"""
URL configuration for myproject project.

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
from myapp_lek3.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('hw1/', include('myapp_hw1.urls')),
    path('hw2/', include('myapp_hw2.urls')),
    path('sem1/', include('myapp_sem1.urls')),
    path('lek1/', include('myapp_lek1.urls')),
    path('lek2/', include('myapp_lek2.urls')),
    path('lek3/', include('myapp_lek3.urls')),
    path('lek4/', include('myapp_lek4.urls')),
]
