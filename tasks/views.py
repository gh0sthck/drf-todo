from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.list import ListView

from .models import TodoList
from .forms import AddTodoListForm


class TodoListView(ListView):
    template_name = "todolists.html"
    context_object_name = "todolists"

    def get_queryset(self) -> QuerySet[Any]:
        return TodoList.objects.filter(author=self.request.user)


class AddTodoListView(View):
    form_class = AddTodoListForm
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.author = self.request.user
            f.save()
            return redirect("my_lists")
    
    def get(self, request, *args, **kwargs):
        return render(request, "todolists_add.html", {"form": self.form_class})
