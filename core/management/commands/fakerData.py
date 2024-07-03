# your_app/management/commands/populate_books.py
from django.core.management.base import BaseCommand
from core.models import Books
from faker import Faker

class Command(BaseCommand):
    help = 'Populate the Books model with fake data'

    def handle(self, *args, **kwargs):
        faker = Faker()
        for i in range(1, 100000):
            print(f"{i} Book is added.....")
            Books.objects.create(
                title=faker.sentence(),
                author=faker.name(),
                publisher_name=faker.company()
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated the Books model with fake data'))
