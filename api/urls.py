from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from .views import SubscriptionViewSet, TaskViewSet, TodoListViewSet, UserViewSet

router = DefaultRouter()

router.register("tasks", TaskViewSet)
router.register("todo_lists", TodoListViewSet)
router.register("users", UserViewSet)
router.register("subscriptions", SubscriptionViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="ToDo List DRF App",
      default_version='v1',
      description="Default todo app with django rest framework",
      contact=openapi.Contact(url="https://github.com/gh0sthck/"),
      license=openapi.License(name="GNU License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns.extend(router.urls)
