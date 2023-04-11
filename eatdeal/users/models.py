from django.contrib.auth.models import AbstractUser
from django.db import models

from api.models import Promo


class User(AbstractUser):
    favorites = models.ManyToManyField(
        Promo, 'favorited', blank=True
    )
