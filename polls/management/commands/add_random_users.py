from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('argum', type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        num = options['argum']

        for _ in range(num):
            user = fake.name().replace(' ', '_').replace("'", '')
            fake_email = fake.ascii_email()
            passw = fake.password()
            User.objects.create_user(
                username=user,
                email=fake_email,
                password=passw
                )

        self.stdout.write(self.style.SUCCESS('ADD USERS'))
