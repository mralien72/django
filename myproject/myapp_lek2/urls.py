from django.urls import path
from . import views

urlpatterns = [
    path('lek2', views.index, name='index'),
]