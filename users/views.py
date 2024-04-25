from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.shortcuts import redirect, render

from users.models import SiteClient

from .forms import UserRegisterForm


def register(request: HttpRequest):
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            passw = f.password
            f.set_password(passw)
            f.save()
            login(request, user=f)
            return redirect("my_lists")
    else:        
        form = UserRegisterForm()
        return render(request, "users_register.html", {"form": form})
