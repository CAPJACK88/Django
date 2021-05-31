from django.db import models
from user.models import User, Position
from django_ckeditor_5.fields import CKEditor5Field
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    name = models.CharField(max_length=500, verbose_name='Имя')
    surname = models.CharField(max_length=500, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=500, blank=True, verbose_name='Отчество')
    email = models.EmailField(max_length=500, unique=True, verbose_name='Почта')
    telephone = PhoneNumberField(blank=True, unique=True, verbose_name='Телефон')
    mobile_phone = PhoneNumberField(blank=True, unique=True, verbose_name='Мобильный телефон')
    url = models.URLField(max_length=200, blank=True, verbose_name='Веб-сайта')
    date_birth = models.DateField(blank=True, verbose_name='Дата рождения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    company = models.ManyToManyField('Company', blank=True, verbose_name='Компания')
    position = models.ManyToManyField('user.Position', blank=True, verbose_name='Должность')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    comment = CKEditor5Field(max_length=500, blank=True, verbose_name='Комментарий')
    publications = models.BooleanField(default=False, verbose_name='Опубликовоно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['date_creation']


class Company(models.Model):
    name = models.CharField(max_length=500, verbose_name='Название', help_text='ООО "НПО "АГАТ"')
    inn = models.CharField(max_length=50, verbose_name='ИНН')
    kpp = models.CharField(max_length=50, unique=True, verbose_name='КПП')
    address = models.TextField(max_length=500, blank=True, verbose_name='Адрес',
                               help_text='196247, Российская Федерация, город Санкт-Петербург, площадь Конституции, '
                                         'дом 2')
    telephone = PhoneNumberField(blank=True, verbose_name='Телефон')
    photo = models.ImageField(upload_to='logo/%Y/%m/%d/', blank=True, verbose_name='Логотип')
    card = models.FileField(upload_to='card/%Y/%m/%d/', blank=True, verbose_name='Карточка')
    url = models.URLField(max_length=200, blank=True, verbose_name='Веб-сайта')
    fixed = models.ManyToManyField('user.User', blank=True, verbose_name='Закреплено')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    comment = CKEditor5Field(max_length=500, blank=True, verbose_name='Комментарий')
    publications = models.BooleanField(default=False, verbose_name='Опубликовоно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['date_creation']
