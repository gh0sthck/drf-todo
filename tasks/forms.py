from django import forms

from .models import TodoList


class AddTodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ["title", "tasks_max_count"]
