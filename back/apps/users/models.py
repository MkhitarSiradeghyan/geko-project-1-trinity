from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        USER = "USER", "User"


    email = models.EmailField(
        unique=True,
        blank=False,
    )


    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=Roles.USER,
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.username


    @property
    def is_admin(self):
        return self.role == self.Roles.ADMIN