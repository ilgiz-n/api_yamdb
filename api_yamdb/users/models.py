from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.conf import settings


class User(AbstractUser):
    status = models.IntegerField(choices=settings.USER_LEVEL_CHOICES, blank=True, default = 3)
