from django.db.models import Prefetch
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from api.serializers import SubscriptionSeializer, TaskSerializer, TodoListSerializer, UserSerializer
from tasks.models import TodoList, Task
from users.models import SiteClient, Subscription


class TodoListViewSet(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return TodoList.objects.filter(author=self.request.user).prefetch_related("tags")
    

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(todo_list__author=self.request.user).prefetch_related(
            Prefetch("todo_list", TodoList.objects.prefetch_related("tags"))
        )


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSeializer
    queryset = Subscription.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = SiteClient.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().list(request, *args, **kwargs)
        else:
            return Response({"detail": "You not admin."}, status=403)
