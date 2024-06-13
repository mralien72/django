from django.core.management.base import BaseCommand
from myapp_hw2.models import Product


class Command(BaseCommand):
    help = "get all product"

    def handle(self, *args, **kwargs):
        product = Product.objects.all()
        self.stdout.write(f'{product}')
