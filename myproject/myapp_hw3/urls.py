from django.urls import path
from .views import all_orders, orders_by_days

app_name = 'myapp_hw3'
urlpatterns = [
    path('allorders/', all_orders, name='all_orders'),
    path('days/<int:user_id>/<int:days>', orders_by_days, name='orders_by_days'),
]