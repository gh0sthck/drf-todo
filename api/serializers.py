from django.contrib.auth.models import User
from rest_framework import serializers

from tasks.models import TodoList, Task


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ["id", "title", "author", "tasks"]
        extra_kwargs = {"tasks": {"read_only": True}}


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "is_completed", "todo_list"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}
    
