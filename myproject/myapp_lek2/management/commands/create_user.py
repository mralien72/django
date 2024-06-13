from django.core.management.base import BaseCommand
from myapp_lek2.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='Neo', email='Neo@example.com', password='secret', age=35)
        user.save()
        self.stdout.write(f'{user}')
