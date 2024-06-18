from django.core.management.base import BaseCommand
from myapp_hw3.models import Order, User, Product
from random import choice, uniform, sample
from datetime import timedelta, datetime

class Command(BaseCommand):
    help = "Create fake orders"

    def add_arguments(self, parser):
        parser.add_argument('num_orders', type=int, help='Number of orders to create')

    def handle(self, *args, **options):
        num_orders = options['num_orders']
        create_fake_orders(num_orders)

def create_fake_orders(num_orders):
    users = list(User.objects.all())
    products = list(Product.objects.all())

    for _ in range(num_orders):
        customer = choice(users)
        order = Order(
            customer=customer,
            total_price=0,
            date_ordered=datetime.now() - timedelta(days=choice(range(30)))
        )
        order.save()

        num_products = choice(range(1, 6))
        order_products = sample(products, num_products)
        for product in order_products:
            order.products.add(product)
            order.total_price += product.price
        order.save()

    print(f"Создано {num_orders} фиктивных заказов.")
