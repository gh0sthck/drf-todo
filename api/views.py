from django.contrib.auth.models import User
from rest_framework import viewsets

from api.serializers import TaskSerializer, TodoListSerializer, UserSerializer
from tasks.models import TodoList, Task


class TodoListViewSet(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()
    

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
