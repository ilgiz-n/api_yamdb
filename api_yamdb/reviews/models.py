from django.db import models
# from django.contrib.auth import get_user_model
# Create your models here.
# User = get_user_model() - заменил на кастомную модель 
from users.models import User


class Comments(models.Model):
    review = models.ForeignKey(
        Reviews,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


class Categories(models.Model):
    name = models.CharField(
        'Name', blank=True, max_length=50
    )
    slug = models.SlugField(
        'Slug', unique=True
    )

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Категория произведения'
        verbose_name_plural = 'Категории произведений'

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(
        'Name', max_length=50
    )
    slug = models.SlugField(
        'Slug', unique=True
    )

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Жанр произведения'
        verbose_name_plural = 'Жанры произведений'

    def __str__(self):
        return self.name


class Titles(models.Model):
    name = models.CharField(
        verbose_name='Название', max_length=200
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
        blank=True, null=True
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
#       related_name='сategories',
        blank=True, null=True,
        verbose_name='Категория',
        help_text='Выберите категорию произведения'
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг',
        blank=True, null=True,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True,
    )
    genre = models.ManyToManyField(
        Genres,
        blank=True,
#       related_name='genres',
        verbose_name='Жанр'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
 
class Reviews(models.Model):
    title = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    score = models.IntegerField(
        blank=True, null=True,
    )
    pub_date = models.DateTimeField(auto_now_add=True)
