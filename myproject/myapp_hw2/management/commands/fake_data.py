from django.core.management.base import BaseCommand
from myapp_hw2.models import User, Product

class Command(BaseCommand):
    help = "Generate fake user, order, and product data."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            user = User(name=f'Name{i}', email=f'mail{i}@mail.ru', phone=f'+7922000{i}{i}{i}{i}', address=f'Address{i}')
            product = Product(name=f'Tovar{i}', price=f'{i}', description=f'Description{i}', quantity_products=f'{i}')
            user.save()
            product.save()