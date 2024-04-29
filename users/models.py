from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class Subscription(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    max_todolists = models.PositiveIntegerField(validators=[
        MaxValueValidator(limit_value=50)
    ], default=0)
    max_tasks_by_list = models.IntegerField(validators=[
        MinValueValidator(0), MaxValueValidator(50)
    ], default=0)
    
    def __repr__(self) -> str:
        return f"<Subscription: {self.name}>"
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["-name"]
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"


class SiteClient(AbstractUser):
    username = models.CharField(max_length=128, unique=True, null=False)
    email = models.EmailField()
    avatar = models.ImageField(
        upload_to="",
        null=True,
        blank=True
    )
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_DEFAULT, default=None,
                                    null=True, related_name="clients")
    
    def __repr__(self) -> str:
        return f"<SiteClient {self.username}>"

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        ordering = ["-username"]
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
