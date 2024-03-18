from django.contrib import admin

from .models import Task, TodoList


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "is_completed", "todo_list"]
    list_filter = ["is_completed", "todo_list"]


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ["title", "tasks_max_count"]
