from http import client
from django import forms

from .models import SiteClient


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=120, widget=forms.PasswordInput(), label="Пароль")
    
    class Meta:
        model = SiteClient
        fields = ["username", "password", "email", "avatar"]
        
    
