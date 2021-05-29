from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'login', 'placeholder': 'ЛОГИН'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'ПАРОЛЬ'}))
