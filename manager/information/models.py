from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse_lazy
from user.models import User


class Information(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название')
    text = CKEditor5Field(max_length=1000, verbose_name='Текст')
    category = models.ManyToManyField('Category', verbose_name='Категория')
    fixed = models.ManyToManyField('user.User', blank=True, verbose_name='Информатор')
    document = models.FileField(upload_to='files/%Y/%m/%d/', blank=True, verbose_name='Документ')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    comment = CKEditor5Field(max_length=1000, blank=True, verbose_name='Комментарий')
    publications = models.BooleanField(default=True, verbose_name='Опубликовоно')

    def get_absolute_url(self):
        return reverse_lazy('________', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информации'
        ordering = ['-date_creation']


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название')
    description = CKEditor5Field(max_length=1000, blank=True, verbose_name='Описание')

    def get_absolute_url(self):
        return reverse_lazy('_______', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
