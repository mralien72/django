from django.core.management.base import BaseCommand
from myapp_hw3.models import User, Product

class Command(BaseCommand):
    help = "Generate fake user, order, and product data."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            user = User(name=f'name{i}', email=f'mail{i}@mail.ru', phone=f'+7922000{i}{i}{i}{i}', address=f'address{i}')
            product = Product(name=f'tovar{i}', price=f'{i}', description=f'description{i}', quantity_products=f'{i}')
            user.save()
            product.save()