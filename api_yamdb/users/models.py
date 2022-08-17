from django.contrib.auth.models import AbstractUser
from django.db import models

USER_LEVEL_CHOICES = (
    ('admin', 'admin'),
    ('moderator', 'moderator'),
    ('user', 'user'),
)

DEFAULT_USER_LEVEL = 'user'

CONFIRMATION_CODE_LENGTH = 5


class User(AbstractUser):
    role = models.CharField(
        max_length=50,
        choices=USER_LEVEL_CHOICES,
        blank=True,
        default=DEFAULT_USER_LEVEL,
        verbose_name="Роль",
    )
    bio = models.TextField(
        blank=True,
        verbose_name="Биография",
    )
    confirmation_code = models.CharField(
        max_length=CONFIRMATION_CODE_LENGTH,
        blank=True,
        verbose_name="Код верификации",
    )
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == "admin"

    @property
    def is_moderator(self):
        return self.role == "moderator"

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
