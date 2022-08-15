import csv
from urllib.parse import urljoin

from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import (Categories, Comments, Genres, GenreTitle, Reviews,
                            Titles)
from users.models import User

DATA = {
    Categories: 'category.csv',
    Comments: 'comments.csv',
    Genres: 'genre.csv',
    GenreTitle: 'genre_title.csv',
    Reviews: 'review.csv',
    Titles: 'titles.csv',
    User: 'users.csv'
}

DATA_DIR = f'{settings.BASE_DIR}/static/data/'


class Command(BaseCommand):
    help = "Загружает тестовые данные."

    def handle(self, *args, **options):
        for model, file in DATA.items():
            path = urljoin(DATA_DIR, file)
            # with open(file_path, 'r', encoding='utf-8') as csv_file:
            with open(path) as csv_file:
                reader = csv.DictReader(csv_file)
                model.objects.bulk_create(model(**data) for data in reader)
                self.stdout.write(
                    self.style.SUCCESS("Тестовыe данные загружены."))
