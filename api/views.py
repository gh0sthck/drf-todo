from rest_framework import permissions, viewsets
from rest_framework.response import Response

from api.serializers import TaskSerializer, TodoListSerializer, UserSerializer
from tasks.models import TodoList, Task
from users.models import SiteClient


class TodoListViewSet(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = TodoList.objects.prefetch_related("tags")
    

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.select_related("todo_list")
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = SiteClient.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().list(request, *args, **kwargs)
        else:
            return Response({"detail": "You not admin."}, status=403)
