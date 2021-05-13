from django.contrib import admin

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):  # Класс для таблицы вывода
    list_display = ('id', 'title', 'category', 'created_at', 'update_at', 'is_published')  # Форматирование таблицы вывода в
    # админке
    list_display_links = ('id', 'title')  # Поля таблицы в админке являющиеся ссылками
    search_fields = ('title', 'content')  # Поля таблицы в админке по которым можно проводить поиск
    list_filter = ('category',)  # Утанавливаем в админки фильтры по параметру Категория
    list_editable = ('is_published',)  # Утанавливаем возможность редактирования прямо из таблицы


class CategoryAdmin(admin.ModelAdmin):  # Класс для таблицы вывода
    list_display = ('id', 'title')  # Форматирование таблицы вывода в админке
    list_display_links = ('id', 'title')  # Поля таблицы в админке являющиеся ссылками
    search_fields = ('title',)  # Поля таблицы в админке по которым можно проводить поиск


admin.site.register(News, NewsAdmin)  # Регистрируем модель в админке. Регистрируем класс изменения вывода
# представвления таблицы в админке
admin.site.register(Category, CategoryAdmin)
