from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role_choices =(
        ('customer','Customer'),
        ('owner','Hotel Owner'),
        ('admin','Admin'),
    )
    role = models.CharField(max_length=20,choices=role_choices,default='customer')
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username