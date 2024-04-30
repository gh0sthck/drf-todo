from django.contrib.auth import login
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from users.models import SiteClient, Subscription

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

    def get(self, request: HttpRequest):
        return render(request, "users_register.html", {"form": self.form()})


class Subscriptions(View):
    subs = Subscription.objects.all()

    subb = [
        [
            sub.name,
            sub.add_todolists,
            sub.add_todolists + SiteClient.DEFAULT_TODOLISTS,
            sub.add_tasks_by_list,
            sub.add_tasks_by_list + SiteClient.DEFAULT_TASKS_BY_LIST,
        ]
        for sub in subs
    ]

    def get(self, request: HttpRequest):
        return render(
            request,
            "users_subscriptions.html",
            {
                "subs": self.subb,
            },
        )
