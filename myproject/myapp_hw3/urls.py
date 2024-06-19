from django.urls import path
from .views import all_orders, orders_by_7days, orders_by_30days, orders_by_365days

app_name = 'myapp_hw3'
urlpatterns = [
    path('allorders/', all_orders, name='all_orders'),
    path('7days/<int:user_id>', orders_by_7days, name='orders_by_7days'),
    path('30days/<int:user_id>', orders_by_30days, name='orders_by_30days'),
    path('365days/<int:user_id>', orders_by_365days, name='orders_by_365days'),
]