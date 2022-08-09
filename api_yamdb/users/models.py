from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.conf import settings


class User(AbstractUser):
    status = ArrayField(
        models.IntegerField(choices=settings.USER_LEVEL_CHOICES, blank=True),
    )

    def __str__(self):
        return self.title