import csv
import os

from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import (Categories, Comments, Genres, GenreTitle, Review,
                            Title)
from users.models import User

path = f'{settings.BASE_DIR}/static/data/'
os.chdir(path)


class Command(BaseCommand):
    def handle(self, *args, **options):

        with open('users.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj = User(
                    id=row['id'],
                    username=row['username'],
                    email=row['email'],
                    role=row['role'],
                    bio=row['bio'],
                    first_name=row['first_name'],
                    last_name=row['last_name']
                )
                obj.save()

        with open('category.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj = Categories(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug']
                )
                obj.save()

        with open('genre.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj = Genres(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug']
                )
                obj.save()

        with open('titles.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj = Title(
                    id=row['id'],
                    name=row['name'],
                    year=row['year'],
                    category=Categories.objects.get(id=row['category'])
                )
                obj.save()

        with open('genre_title.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj = GenreTitle(
                    id=row['id'],
                    title=Title.objects.get(id=row['title_id']),
                    genre=Genres.objects.get(id=row['genre_id'])
                )
                obj.save()

        with open('review.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj = Review(
                    id=row['id'],
                    title=Title.objects.get(id=row['title_id']),
                    text=row['text'],
                    author=User.objects.get(id=row['author']),
                    score=row['score'],
                    pub_date=row['pub_date']
                )
                obj.save()

        with open('comments.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj = Comments(
                    id=row['id'],
                    review=Review.objects.get(id=row['review_id']),
                    text=row['text'],
                    author=User.objects.get(id=row['author']),
                    pub_date=row['pub_date']
                )
                obj.save()

        self.stdout.write(
            self.style.SUCCESS("Тестовыe данные загружены."))
