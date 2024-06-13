from django.core.management.base import BaseCommand
from myapp_hw2.models import Product


class Command(BaseCommand):
    help = "Update price product"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('description', type=str, help='description product')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        product = Product.objects.filter(name=name).first()
        if product:
            product.description = description
            product.save()
            self.stdout.write(f'{product}')
        else:
            self.stdout.write(f'Product with name "{name}" not found.')
