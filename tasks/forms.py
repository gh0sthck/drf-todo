from django import forms

from .models import Task, TodoList


class AddTodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ["title"]
        

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]
