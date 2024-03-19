import datetime

from pytils.translit import slugify

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название тега", unique=True)
    
    class Meta:
        ordering = ["-name"]
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
    
    def __str__(self) -> str:
        return f"<Tag: {self.name}>"


class TodoList(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название списка задач")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    tags = models.ManyToManyField(Tag, related_name="todolists", verbose_name="Теги", null=True,
                                  blank=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    slug = models.SlugField(verbose_name="Слаг")
    
    class Meta:
        ordering = ["-title"]
        verbose_name = "Список задач"
        verbose_name_plural = "Списки задач"
        
    def get_completed_tasks(self) -> ...:
        tasks = self.tasks.filter(is_completed=True)
        return tasks
    
    def get_absolute_url(self):
        return reverse("current_list", kwargs={"slug": self.slug})
    
    
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        return super(TodoList, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"<TodoList: {self.title}>"


class Task(models.Model):
    title = models.CharField(max_length=256, verbose_name="Задача")
    description = models.TextField(verbose_name="Описание задачи", null=True, blank=True)
    is_completed = models.BooleanField(default=False, verbose_name="Выполнено")
    todo_list = models.ForeignKey(TodoList, related_name="tasks", on_delete=models.CASCADE, 
                                  verbose_name="Список задач")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания задачи",
                                       blank=True)
    complete_date = models.DateTimeField(verbose_name="Дата завершения задачи",
                                         default=None, null=True, blank=True)
    
    
    class Meta:
        ordering = ["-title", "is_completed"]
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
    
    def save(self, *args, **kwargs) -> None:
        if self.is_completed:
            self.complete_date = datetime.datetime.now()
        return super(Task, self).save(*args, **kwargs)
        
    def get_read_status(self) -> str:
        return "Выполнено" if self.is_completed else "Не выполнено"
        
    def __str__(self) -> str:
        return f"<Task: {self.title}>"
