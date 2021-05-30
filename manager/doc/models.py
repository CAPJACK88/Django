from django.db import models
from django.urls import reverse_lazy
from user.models import User, Position


class Document(models.Model):
    title = models.CharField(max_length=500, unique=True, verbose_name='Название')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    document = models.FileField(upload_to='files/%Y/%m/%d/', verbose_name='Документ')
    publications = models.BooleanField(default=False, verbose_name='Опубликовоно')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    username = models.ManyToManyField('user.User', blank=True, verbose_name='Имя')

    def get_absolute_url(self):
        return reverse_lazy('DocList', kwargs={'document.url': self.document.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['date_creation']


class Category(models.Model):
    title = models.CharField(max_length=500, unique=True, verbose_name='Название')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')

    def get_absolute_url(self):
        return reverse_lazy('CategoryList', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
