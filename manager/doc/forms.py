from django import forms
from .models import Document, Category, User
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'login', 'placeholder': 'ЛОГИН'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'ПАРОЛЬ'}))
