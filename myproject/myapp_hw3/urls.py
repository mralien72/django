from django.urls import path
from .views import all_orders, orders_by_7days

app_name = 'myapp_hw3'
urlpatterns = [
    path('allorders/', all_orders, name='all_orders'),
    path('7days/<int:user_id>', orders_by_7days, name='orders_by_7days'),
    # path('allorders/', views.all_orders, name='all_orders'),
    # path('allorders/', views.all_orders, name='all_orders'),
]