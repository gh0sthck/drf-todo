from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import Register, Subscriptions

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users_login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", Register.as_view(), name="register"),
    path("subscriptions/", Subscriptions.as_view(), name="subscriptions")
]
