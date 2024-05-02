from django.db.models import Prefetch
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from api.serializers import (
    SubscriptionSeializer,
    TaskSerializer,
    TodoListSerializer,
    UserSerializer,
)
from tasks.models import TodoList, Task
from users.models import SiteClient, Subscription


class TodoListViewSet(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TodoList.objects.filter(author=self.request.user).prefetch_related(
            "tags"
        )


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(
            todo_list__author=self.request.user
        ).prefetch_related(
            Prefetch("todo_list", TodoList.objects.prefetch_related("tags"))
        )


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSeializer
    queryset = Subscription.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SiteClient.objects.prefetch_related(
            Prefetch("subscription", Subscription.objects.all().only("name"))
        ).filter(pk=self.request.user.pk)

    def retrieve(self, request, pk=None):
        if self.request.user.is_superuser:
            data = SiteClient.objects.filter(pk=pk).prefetch_related(
                Prefetch("subscription", Subscription.objects.all().only("name"))
            )
            data_formatted = [UserSerializer(user).data for user in data]
            return Response(data=data_formatted, status=200)
        else:
            return Response(
                {"detail": "You havn't permissions to this operation."}, status=403
            )
