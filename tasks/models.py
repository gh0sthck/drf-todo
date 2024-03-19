from typing import Any
from django.db import models
from django.contrib.auth.models import User


class TodoList(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название списка задач")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    
    class Meta:
        ordering = ["-title"]
        verbose_name = "Список задач"
        verbose_name_plural = "Списки задач"
        
    def get_completed_tasks(self) -> ...:
        tasks = self.task_set.filter(is_completed=True)
        return tasks
    
    def __str__(self) -> str:
        return f"<TodoList: {self.title}>"


class Task(models.Model):
    title = models.CharField(max_length=256, verbose_name="Задача")
    description = models.TextField(verbose_name="Описание задачи", null=True)
    is_completed = models.BooleanField(default=False, verbose_name="Выполнено")
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, 
                                  verbose_name="Список задач")
    
    class Meta:
        ordering = ["-title", "is_completed"]
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        
    def __str__(self) -> str:
        return f"<Task: {self.title}>"
