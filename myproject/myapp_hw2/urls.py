from django.urls import path
from . import views

app_name = 'myapp_hw2'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]