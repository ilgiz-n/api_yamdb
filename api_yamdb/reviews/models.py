from django.db import models


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
#        related_name='сategories',
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
#        related_name='genres',
        verbose_name='Жанр'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Произведение'

    def __str__(self):
        return self.name
