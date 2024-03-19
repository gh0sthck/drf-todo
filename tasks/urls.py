from django.urls import path

from .views import AddTodoListView, TodoListView

urlpatterns = [
    path("my_lists/", TodoListView.as_view(), name="my_lists"),
    path("create_todolist/", AddTodoListView.as_view(), name="create_todolist")
]
