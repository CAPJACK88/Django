from django.db import models


# Create your models here.

class User(models.Model):
    name_user = models.CharField(max_length=200, verbose_name="Имя")
    mail_user = models.EmailField(max_length=200, verbose_name='email')
    password_user = models.CharField(max_length=50, verbose_name='Пароль')
