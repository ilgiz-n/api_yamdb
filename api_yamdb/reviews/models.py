from django.db import models
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


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
        related_name='сategories',
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
        related_name='genres',
        verbose_name='Жанр',
        through='GenreTitle'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    title = models.ForeignKey(Titles, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title}, {self.genre}'


class Reviews(models.Model):
    title = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.IntegerField(
        validators=[
            MinValueValidator(1, 'Оценка должна быть не меньше 1.'),
            MaxValueValidator(10, 'Оценка должна быть не больше 10.')
        ],
        verbose_name='Оценка произведения')
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pub_date']
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_review'
            ),
        ]


class Comments(models.Model):
    review = models.ForeignKey(
        Reviews,
        on_delete=models.SET_NULL,
        null=True,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
