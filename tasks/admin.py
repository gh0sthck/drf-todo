from django.contrib import admin

from .models import Task, TodoList


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title",  "is_completed", "todo_list",
                    "complete_date", "create_date"]
    list_filter = ["is_completed", "todo_list", "complete_date", "create_date"]


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "create_date"]
