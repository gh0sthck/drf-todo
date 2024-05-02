from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from tasks.models import TodoList, Task
from users.models import SiteClient, Subscription


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "is_completed",
            "todo_list",
            "create_date",
            "complete_date",
            "priority",
        ]


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


class SubscriptionSeializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["name", "add_todolists", "add_tasks_by_list"]


class UserSerializer(serializers.ModelSerializer):
    subscription = serializers.CharField(source="subscription.name", default=None)
        
    class Meta:
        model = SiteClient
        fields = [
            "id",
            "username",
            "email",
            "password",
            "max_list_default",
            "max_tasks_by_list_default",
            "subscription",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "subscription": {"read_only": True},
        }
