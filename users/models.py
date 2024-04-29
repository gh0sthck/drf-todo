from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class Subscription(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    add_todolists = models.PositiveIntegerField(validators=[
        MinValueValidator(0), MaxValueValidator(limit_value=50)
    ], default=0)
    add_tasks_by_list = models.IntegerField(validators=[
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
    max_list_default = models.PositiveIntegerField(default=5, null=False)
    max_tasks_by_list_default = models.PositiveIntegerField(default=10, null=False)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL,
                                    null=True, blank=True, related_name="clients")
    
    def get_max_lists(self) -> int:
        return self.max_list_default + (self.subscription.add_todolists if self.subscription else 0)
    
    def get_max_tasks_by_list(self) -> int:
        return self.max_tasks_by_list_default + (self.subscription.add_tasks_by_list \
            if self.subscription else 0)
    
    def __repr__(self) -> str:
        return f"<SiteClient {self.username}>"

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        ordering = ["-username"]
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
