from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):  # Класс для таблицы вывода
    list_display = ('id', 'title', 'category', 'created_at', 'update_at', 'is_published', 'get_photo')  # Форматирование таблицы вывода в админке
    list_display_links = ('id', 'title')  # Поля таблицы в админке являющиеся ссылками
    search_fields = ('title', 'content')  # Поля таблицы в админке по которым можно проводить поиск
    list_filter = ('category',)  # Утанавливаем в админки фильтры по параметру Категория
    list_editable = ('is_published',)  # Утанавливаем возможность редактирования прямо из таблицы
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'views', 'created_at', 'update_at')  # Утанавливаем отображение в конкретной новости
    readonly_fields = ('get_photo', 'views', 'created_at', 'update_at')  # Утанавливаем графы только для чтения
    save_on_top = True  # Добавляем кнопки сохранить вверх

    def get_photo(self, obj):  # Возвращаем миниатюру взамен ссылки
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Нет фото'
    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):  # Класс для таблицы вывода
    list_display = ('id', 'title')  # Форматирование таблицы вывода в админке
    list_display_links = ('id', 'title')  # Поля таблицы в админке являющиеся ссылками
    search_fields = ('title',)  # Поля таблицы в админке по которым можно проводить поиск


admin.site.register(News, NewsAdmin)  # Регистрируем модель в админке. Регистрируем класс изменения выводапредставвления таблицы в админке
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Уапавление новостями'
admin.site.site_header = 'Уапавление новостями'
