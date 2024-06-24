from django.urls import path
from .views import all_orders, orders_by_days, product_cart, product_create

app_name = 'myapp_hw3'
urlpatterns = [
    path('allorders/', all_orders, name='all_orders'),
    path('product/<int:product_id>/', product_cart, name='product_cart'),
    path('product_create/', product_create, name='product_create'),
    # path('upload/<int:product_id>/', upload_image, name='upload_image'),
    path('days/<int:user_id>/<int:days>', orders_by_days, name='orders_by_days'),
]