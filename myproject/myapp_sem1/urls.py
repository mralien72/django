from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coin/', views.coin, name='coin'),
    path('random_roll/', views.random_roll, name='random_roll'),
    path('random_number/', views.random_number, name='random_number'),
    ]
