from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from tasks.models import TodoList, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "is_completed", "todo_list"]


class TodoListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username")
    
    def create(self, validated_data):
        user_id: int = validated_data["author"]["username"]
        validated_data["author"] = get_object_or_404(User, id=user_id)
        tl = TodoList(**validated_data)
        tl.save()
        return tl
    
    class Meta:
        model = TodoList
        fields = ["id", "title", "author", "tasks"] 
        read_only_fields = ["tasks"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}
    
