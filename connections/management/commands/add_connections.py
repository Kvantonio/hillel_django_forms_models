from connections.models import Author, Book, Description,  Publisher

from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('argum', type=int)

    def handle(self, *args, **options):
        num = options['argum']
        for _ in range(int(num/10)):
            pub = Publisher.objects.create(pub_title=fake.company())
            for _ in range(int(num/200)):
                a = Author.objects.create(name=fake.name())
                for _ in range(2):
                    b = Book.objects.create(
                        title=fake.sentence(nb_words=3,
                                            variable_nb_words=True
                                            ).replace('.', ''),
                        publishing=pub
                    )
                    b.author_set.add(a)
                    Description.objects.create(
                        text=fake.paragraph(nb_sentences=5),
                        book=b)
        self.stdout.write(self.style.SUCCESS('ADD CONNECTIONS'))
