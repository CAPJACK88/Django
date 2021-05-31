from django.db import models
from cont.models import Company
from user.models import User
from django_ckeditor_5.fields import CKEditor5Field


class Contract(models.Model):
    number = models.CharField(max_length=50, unique=True, verbose_name='Номер')
    company = models.ManyToManyField('cont.Company', blank=True, verbose_name='Компания')
    fixed = models.ManyToManyField('user.User', blank=True, verbose_name='Закреплено')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    comment = CKEditor5Field(max_length=500, blank=True, verbose_name='Комментарий')
    publications = models.BooleanField(default=True, verbose_name='Опубликовоно')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'
        ordering = ['-date_creation']
