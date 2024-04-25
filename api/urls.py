from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, TodoListViewSet, UserViewSet

router = DefaultRouter()

router.register("tasks", TaskViewSet)
router.register("todo_lists", TodoListViewSet, basename="todo-lists")
router.register("users", UserViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)
