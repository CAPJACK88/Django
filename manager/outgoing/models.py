from django.db import models
from django.urls import reverse_lazy
from django_ckeditor_5.fields import CKEditor5Field
from cont.models import Company
from user.models import User


class Outgoing(models.Model):
    number = models.CharField(max_length=255, unique=True, verbose_name='Исходящий')
    company = models.ManyToManyField('cont.Company', blank=True, verbose_name='Компания')
    company_02 = models.CharField(max_length=255, verbose_name='Компания (Быстрая запись)')
    fixed = models.ManyToManyField('user.User', blank=True, verbose_name='Закреплено')
    document = models.FileField(upload_to='files/%Y/%m/%d/', blank=True, verbose_name='Документ')
    CategoryOutgoing = models.ManyToManyField('CategoryOutgoing',blank=True, verbose_name='Каиегория')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    comment = CKEditor5Field(max_length=1000, blank=True, verbose_name='Комментарий')
    publications = models.BooleanField(default=True, verbose_name='Опубликовоно')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Исходящий'
        verbose_name_plural = 'Исходящие'
        ordering = ['-date_creation']


class CategoryOutgoing(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название')
    description = CKEditor5Field(max_length=1000, blank=True, verbose_name='Описание')

    def get_absolute_url(self):
        return reverse_lazy('CategoryList', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']