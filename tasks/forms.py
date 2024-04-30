from django import forms
from django.forms import widgets

from .models import Task, TodoList

ADD_TASK_CHOICES = {i: i for i in range(1, 6)}


class AddTodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ["title"]


class AddTaskForm(forms.ModelForm):
    priority = forms.IntegerField(
        max_value=5,
        min_value=1,
        label="Приоритет",
        widget=forms.Select(choices=ADD_TASK_CHOICES),
    )

    class Meta:
        model = Task
        fields = ["title", "priority"]
