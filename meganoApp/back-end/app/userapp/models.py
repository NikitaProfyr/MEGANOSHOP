from django.contrib.auth.models import User
from django.db import models

# Create your models here.


def load_to_avatar(instance: "Profile", filename: str) -> str:
    return f"users/user_{instance.pk}/avatar_{filename}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userName = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="имя пользователя"
    )
    bio = models.TextField(
        max_length=300, null=True, blank=True, verbose_name="биография"
    )
    balance = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        default=0,
        verbose_name="баланс",
    )
    avatar = models.ImageField(null=True, blank=True, upload_to=load_to_avatar)
