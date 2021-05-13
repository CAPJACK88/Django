from django import forms
from .models import Category, News
# from django.core.files.uploadedfile import SimpleUploadedFile
# from PIL import Image


class NewsForm(forms.Form):
    title = forms.CharField(label='Название', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст новости', required=False, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5
    }))
    # is_published = forms.BooleanField(label='Опубликовано', initial=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-label'}))
    category = forms.ModelChoiceField(label='Категория:', empty_label='Выберите категорию', queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))


class ImageForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'photo')