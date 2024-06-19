from django.shortcuts import render, get_object_or_404
from .models import Order, User
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

def all_orders(request):
    logger.info('Index page accessed')
    orders = list(Order.objects.all())
    return render(request, 'myapp_hw3/all_orders.html', {'orders': orders})


def orders_by_7days(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    last_7_days = timezone.now() - timezone.timedelta(days=7)
    orders_user = Order.objects.filter(customer=user, date_ordered__gte=last_7_days)

    order_products = {}
    for order in orders_user:
        for product in order.products.all():
            if product not in order_products:
                order_products[product] = order.date_ordered
            else:
                order_products[product] = max(order_products[product], order.date_ordered)
# не понял какую дату оставлять при сортировке товара, чтобы он не повторялся,
# по этому прописал чтобы оставался самый послений заказанный товар

    order_products = sorted(order_products.items(), key=lambda x: x[1], reverse=True)
#С лямбдой у меня плохо, по этому нашел такой вариано сортировки и использовал его...

    return render(request, 'myapp_hw3/orders_by_7days.html', {
        'user': user,
        'order_products': order_products,
        })


def orders_by_30days(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    last_30_days = timezone.now() - timezone.timedelta(days=30)
    orders_user = Order.objects.filter(customer=user, date_ordered__gte=last_30_days)

    order_products = {}
    for order in orders_user:
        for product in order.products.all():
            if product not in order_products:
                order_products[product] = order.date_ordered
            else:
                order_products[product] = max(order_products[product], order.date_ordered)
# не понял какую дату оставлять при сортировке товара, чтобы он не повторялся,
# по этому прописал чтобы оставался самый послений заказанный товар

    order_products = sorted(order_products.items(), key=lambda x: x[1], reverse=True)
#С лямбдой у меня плохо, по этому нашел такой вариано сортировки и использовал его...

    return render(request, 'myapp_hw3/orders_by_month.html', {
        'user': user,
        'order_products': order_products,
        })


def orders_by_365days(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    last_365_days = timezone.now() - timezone.timedelta(days=365)
    orders_user = Order.objects.filter(customer=user, date_ordered__gte=last_365_days)

    order_products = {}
    for order in orders_user:
        for product in order.products.all():
            if product not in order_products:
                order_products[product] = order.date_ordered
            else:
                order_products[product] = max(order_products[product], order.date_ordered)
# не понял какую дату оставлять при сортировке товара, чтобы он не повторялся,
# по этому прописал чтобы оставался самый послений заказанный товар

    order_products = sorted(order_products.items(), key=lambda x: x[1], reverse=True)
#С лямбдой у меня плохо, по этому нашел такой вариано сортировки и использовал его...

    return render(request, 'myapp_hw3/orders_by_year.html', {
        'user': user,
        'order_products': order_products,
        })
