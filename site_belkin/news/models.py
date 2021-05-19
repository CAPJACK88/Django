from django.db import models
from django.urls import reverse_lazy  # Импортируем реверс_лези для построение ссылки методом get_absolute_url()


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дада создания')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='Дада обновления')
    photo = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовоно')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True,
                                 verbose_name='Категории')  # Связываем модель с подклассом
    views = models.IntegerField(default=0)

    def get_absolute_url(self):  # Метод для построения маршрута ссылки (первый аргумент 'название маршрута'
        # (фаил urls.pu | name='view_news')
        return reverse_lazy('view_news', kwargs={'pk': self.pk})

    def __str__(self):  # Возвращаем строковое значение title
        return self.title

    class Meta:  # Переименовываем название в админке
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']  # Сортировка по дате в обратном порядке в админке


class Category(models.Model):  # Объявляем КЛАСС
    title = models.CharField(max_length=150, verbose_name='Наименование')

    def get_absolute_url(self):  # Метод для построения маршрута ссылки (первый аргумент 'название маршрута'
        # (фаил urls.pu | name='category')
        return reverse_lazy('category', kwargs={'category_id': self.pk})

    def __str__(self):  # Возвращаем строковое значение title
        return self.title

    class Meta:  # Переименовываем название в админке
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']  # Сортировка по id
