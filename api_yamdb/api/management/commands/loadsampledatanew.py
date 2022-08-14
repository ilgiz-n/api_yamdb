import csv
import os

from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import (Categories, Comments, Genres, GenreTitle, Reviews,
                            Titles)
from users.models import User

path = f'{settings.BASE_DIR}/static/data/'
os.chdir(path)


class Command(BaseCommand):
    def handle(self, *args, **options):
        # User
        with open('users.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = User(
                    id=row['id'],
                    username=row['username'],
                    email=row['email'],
                    role=row['role'],
                    bio=row['bio'],
                    first_name=row['first_name'],
                    last_name=row['last_name']
                )
                p.save()

        # Category
        with open('category.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = Categories(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug']
                )
                p.save()

        # Genre
        with open('genre.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = Genres(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug']
                )
                p.save()

        # Title
        with open('titles.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = Titles(
                    id=row['id'],
                    name=row['name'],
                    year=row['year'],
                    category=Categories.objects.get(id=row['category'])
                )
                p.save()

        # GenreTitle
        with open('genre_title.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = GenreTitle(
                    id=row['id'],
                    title=Titles.objects.get(id=row['title_id']),
                    genre=Genres.objects.get(id=row['genre_id'])
                )
                p.save()

        # Review
        with open('review.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = Reviews(
                    id=row['id'],
                    title=Titles.objects.get(id=row['title_id']),
                    text=row['text'],
                    author=User.objects.get(id=row['author']),
                    score=row['score'],
                    pub_date=row['pub_date']
                )
                p.save()

        # Comment
        with open('comments.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = Comments(
                    id=row['id'],
                    review=Reviews.objects.get(id=row['review_id']),
                    text=row['text'],
                    author=User.objects.get(id=row['author']),
                    pub_date=row['pub_date']
                )
                p.save()

        self.stdout.write(
            self.style.SUCCESS("Тестовыe данные загружены."))
