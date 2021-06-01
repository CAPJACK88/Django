from django.db import models
from user.models import User
from cont.models import Company
from contract.models import Contract
from django_ckeditor_5.fields import CKEditor5Field


class Score(models.Model):
    number = models.CharField(max_length=255, unique=True, verbose_name='Номер')
    company = models.ManyToManyField('cont.Company', blank=True, verbose_name='Компания')
    fixed = models.ManyToManyField('user.User', blank=True, verbose_name='Закреплено')
    contract = models.ManyToManyField('contract.Contract', blank=True, verbose_name='Договор')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    comment = CKEditor5Field(max_length=1000, blank=True, verbose_name='Комментарий')
    production = models.BooleanField(default=False, verbose_name='Производство')
    payment = models.BooleanField(default=False, verbose_name='Оплата')
    publications = models.BooleanField(default=True, verbose_name='Опубликовоно')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
        ordering = ['-date_creation']
