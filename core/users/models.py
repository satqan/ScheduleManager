from django.contrib.auth.models import AbstractUser
from django.db import models
from .choices import UserRoles


class User(AbstractUser):
    role = models.CharField(max_length=10, choices=UserRoles.choices, default=UserRoles.CLIENT)

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.role}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"