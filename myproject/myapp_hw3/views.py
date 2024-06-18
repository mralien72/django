from django.shortcuts import render, get_object_or_404
from .models import Order, User
import logging

logger = logging.getLogger(__name__)

def all_orders(request):
    logger.info('Index page accessed')
    orders = list(Order.objects.all())
    return render(request, 'myapp_hw3/all_orders.html', {'orders': orders})


def orders_by_7days(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders_user = Order.objects.filter(customer=user)


    return render(request, 'myapp_hw3/orders_by_7days.html', {
        'user': user,
        'orders_user': orders_user,
    })

