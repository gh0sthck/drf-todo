from django.views.generic import CreateView
from django.contrib.auth.models import User


class UserRegistration(CreateView):
    model = User
    form = ...
