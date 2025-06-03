from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    tel = models.CharField(max_length=15, blank=True)
    sexe = models.CharField(max_length=10, choices=[
        ('male', 'Homme'),
        ('female', 'Femme'),
    ], blank=True)

    def __str__(self):
        return self.username
# Create your models here.
