from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


DEFAULT_USER_LEVEL = 3

class User(AbstractUser):
    role = models.IntegerField(
        choices=settings.USER_LEVEL_CHOICES, 
        blank=True, 
        default = DEFAULT_USER_LEVEL,
        verbose_name="Роль",
    )
    bio = models.TextField(
        blank=True,
        verbose_name="Биография",
    )
    confirmation_code = models.CharField(
        max_length=settings.CONFIRMATION_CODE_LENGTH,
        blank=True,
        verbose_name="Код верификации",
    )

    def __str__(self):
        return self.username 


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

