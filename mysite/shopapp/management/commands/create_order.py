from django.core.management import BaseCommand
from django.contrib.auth.models import User
from shopapp.models import Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("create order")
        user = User.objects.get(username='admin')
        order = Order.objects.get_or_create(
            delvery_address="sovetskay 20",
            promocode="Sale234",
            user=user,
        )
        self.stdout.write(f'created order {order}')
