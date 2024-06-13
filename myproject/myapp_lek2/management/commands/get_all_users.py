from django.core.management.base import BaseCommand
from myapp_lek2.models import User


class Command(BaseCommand):
    help = "get all users"

    def handle(self, *args, **kwargs):
        user = User.objects.all()
        self.stdout.write(f'{user}')
