from django.urls import path

from .views import AddTodoListView, TodoListView, CurrentTodoListView

urlpatterns = [
    path("my_lists/", TodoListView.as_view(), name="my_lists"),
    path("create_todolist/", AddTodoListView.as_view(), name="create_todolist"),
    path("current_list/<slug:slug>", CurrentTodoListView.as_view(), name="current_list")
]
