from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


DEFAULT_USER_LEVEL = 3

class User(AbstractUser):
    status = models.IntegerField(
        choices=settings.USER_LEVEL_CHOICES, 
        blank=True, 
        default = DEFAULT_USER_LEVEL,
        verbose_name="Роль"
    )
