from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class User(models.Model):
    name = models.CharField(max_length=500, verbose_name='Имя')
    surname = models.CharField(max_length=500, verbose_name='Фамилия')
    email = models.EmailField(max_length=50, unique=True, verbose_name='email')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    position = models.ManyToManyField('Position', blank=True, verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['id']


class Position(models.Model):
    position = models.CharField(max_length=500, unique=True, verbose_name='Должность')
    description = CKEditor5Field(max_length=1000, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['id']
