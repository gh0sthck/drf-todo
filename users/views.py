from django.contrib.auth import login
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from .forms import UserRegisterForm


class Register(View):
    form = UserRegisterForm
    
    def post(self, request: HttpRequest):
        form = self.form(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            passw = f.password
            f.set_password(passw)
            f.save()
            login(request, user=f)
        return redirect("my_lists")

    def get(self, request: HttpRequest,):
        return render(request, "users_register.html", {"form": self.form()})


class Subscriptions(View):
    ...
