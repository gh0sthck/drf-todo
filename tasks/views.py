from typing import Any

from django.db.models import Prefetch
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import ListView

from users.models import SiteClient

from .models import TodoList, Task
from .forms import AddTaskForm, AddTodoListForm


class TodoListView(ListView):
    template_name = "todolists.html"
    context_object_name = "todolists"

    def get_queryset(self) -> QuerySet[Any]:
        return TodoList.objects.filter(author=self.request.user.id)


class CurrentTodoListView(DetailView):
    template_name = "todolist.html"
    model = TodoList
    context_object_name = "list"
    form = AddTaskForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["add_task_form"] = self.form
        return ctx
    
    def get(self, request, *args, **kwargs):
        form = self.form(request.GET)
        if form.data:
            current_task = "".join(form.data.keys())
            t = Task.objects.filter(todo_list=self.get_object(), title=current_task)[0]
            if t.is_completed:
                t.is_completed = False
            else: 
                t.is_completed = True
            t.save()
        return super(CurrentTodoListView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.todo_list = self.get_object()
            f.save()
            return redirect("my_lists")
        return redirect("current_list", self.get_object().slug)


class AddTodoListView(View):
    form_class = AddTodoListForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user_lists_cnt = \
                TodoList.objects.prefetch_related(
                    Prefetch("author", SiteClient.objects.select_related("subscription"))
                ).count()
            if user_lists_cnt < request.user.get_max_lists():
                f = form.save(commit=False)
                f.author = self.request.user
                f.save()
                return redirect("my_lists")
            return redirect("my_lists")
        return redirect("my_lists")

    def get(self, request, *args, **kwargs):
        return render(request, "todolists_add.html", {"form": self.form_class})
