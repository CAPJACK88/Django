from django.db import models


class User(models.Model):
    name_user = models.CharField(max_length=200, unique=True, verbose_name='Имя')
    mail_user = models.EmailField(max_length=200, verbose_name='email')
    password_user = models.CharField(max_length=50, verbose_name='Пароль')

    def __str__(self):  # Возвращаем строковое значение title
        return self.name_user


class Doc(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Название')
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')
    publications = models.BooleanField(default=False, verbose_name='Опубликовоно')
    document = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='Документ')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title, self.description

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        # ordering = ['-created_at']  # Сортировка по дате в обратном порядке в админке


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Название')
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title, self.description

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
