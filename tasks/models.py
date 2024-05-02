import datetime

from typing import List

from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models
from django.urls import reverse

from users.models import SiteClient


class Tag(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название тега", unique=True)

    def __repr__(self) -> str:
        return f"<Tag: {self.name}>"

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["-name"]
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class TodoList(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название задачника")
    author = models.ForeignKey(
        SiteClient, on_delete=models.CASCADE, verbose_name="Автор"
    )
    tags = models.ManyToManyField(
        Tag, related_name="todolists", verbose_name="Теги", blank=True
    )
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def get_completed_tasks(self) -> List["TodoList"]:
        """Return all completed task in TodoList."""
        tasks = self.tasks.filter(is_completed=True)
        return tasks

    def get_absolute_url(self):
        return reverse("current_list", kwargs={"pk": self.pk})

    def __repr__(self) -> str:
        return f"<TodoList: {self.title}>"

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-title"]
        verbose_name = "Список задач"
        verbose_name_plural = "Списки задач"


class Task(models.Model):
    title = models.CharField(max_length=256, verbose_name="Задача")
    is_completed = models.BooleanField(default=False, verbose_name="Выполнено")
    todo_list = models.ForeignKey(
        TodoList,
        related_name="tasks",
        on_delete=models.CASCADE,
        verbose_name="Список задач",
        null=True,  
        blank=True,
        default=None,
    )
    create_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания задачи", blank=True
    )
    complete_date = models.DateTimeField(
        verbose_name="Дата завершения задачи", default=None, null=True, blank=True
    )
    priority = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=1,
        help_text="Приоритет не должен быть больше 5",
        verbose_name="Приоритет",
    )

    def get_read_status(self) -> str:
        """Return readable task status."""
        return "Выполнено" if self.is_completed else "Не выполнено"

    def save(self, *args, **kwargs) -> None:
        if self.is_completed:
            self.complete_date = datetime.datetime.now()
        return super(Task, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"<Task: {self.title}>"

    class Meta:
        ordering = ["-title", "is_completed"]
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
