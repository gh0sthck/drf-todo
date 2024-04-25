from django.db import models
from django.contrib.auth.models import AbstractUser


class SiteClient(AbstractUser):
    username = models.CharField(max_length=128, unique=True, null=False)
    email = models.EmailField()
    avatar = models.ImageField(
        upload_to="",
        null=True,
    )
    
    
    class Meta:
        ordering = ["-username"]
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
