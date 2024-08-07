from django.urls import path
from .views import all_orders, orders_by_days, product_cart, product_create, product_detail, index, all_product

app_name = 'myapp_hw3'
urlpatterns = [
    path('', index, name='index'),
    path('allorders/', all_orders, name='all_orders'),
    path('allproduct/', all_product, name='all_product'),
    path('product/', product_cart, name='product_cart'),
    path('product_create/', product_create, name='product_create'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('days/<int:user_id>/<int:days>', orders_by_days, name='orders_by_days'),
]