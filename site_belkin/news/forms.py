from django import forms
from .models import News
import re  # Модуль регулярных выражений
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='e-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User  # Связываем с моделью User из Django
        fields = ('username', 'email', 'password1', 'password2')


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_title(self):  # Кастомный валидатор
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинатся с цифры')
        return title

# Метод формы несвязанной с Моделью (Необходимо импортировать модель Category)
# class NewsForm(forms.Form):
#     title = forms.CharField(label='Название', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     content = forms.CharField(label='Текст новости', required=False, widget=forms.Textarea(attrs={
#         'class': 'form-control',
#         'rows': 5
#     }))
#     # is_published = forms.BooleanField(label='Опубликовано', initial=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-label'}))
#     category = forms.ModelChoiceField(label='Категория:', empty_label='Выберите категорию', queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
