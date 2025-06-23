from django.core.management import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    """ create product """

    def handle(self, *args, **options):
        self.stdout.write("create product")
        product_names = [
            'laptop',
            'desktop',
            'smartphone',
        ]
        for product_name in product_names:
            product, created = Product.objects.get_or_create(name=product_name)
            self.stdout.write(f"created product: {product.name}")
        self.stdout.write(self.style.SUCCESS("product created"))
