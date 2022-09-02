from random import randrange
from django.core.management import BaseCommand
from faker import Faker
from core.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()

        print("Creating Products with populate_products.py")
        for _ in range(30):
            Product.objects.create(
                title=faker.name(),
                description=faker.text(100),
                image=faker.image_url(),
                price=randrange(10, 100),
            )

            print(f"Products {_} successfully created!")

        print("Products Successfully Created!")


