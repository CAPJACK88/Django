from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Название')
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    document = models.FileField(upload_to='files/%Y/%m/%d/', verbose_name='Документ')
    publications = models.BooleanField(default=False, verbose_name='Опубликовоно')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    username = models.ForeignKey('User', on_delete=models.PROTECT, null=True, verbose_name='Имя')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Название')
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class User(models.Model):
    username = models.CharField(max_length=200, unique=True, verbose_name='Название')
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Имя'
        verbose_name_plural = 'Имена'
