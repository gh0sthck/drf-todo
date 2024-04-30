from django.urls import path

from .views import (
    AddTodoListView,
    DeleteTask,
    DeleteTodoList,
    TodoListView,
    CurrentTodoListView,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="my_lists"),
    path("add_todolist/", AddTodoListView.as_view(), name="create_list"),
    path(
        "current_todolist/<int:pk>",
        CurrentTodoListView.as_view(),
        name="current_list",
    ),
    path("delete_todolist/<int:pk>", DeleteTodoList.as_view(), name="delete_list"),
    path("delete_task/<int:pk>", DeleteTask.as_view(), name="delete_task"),
]
