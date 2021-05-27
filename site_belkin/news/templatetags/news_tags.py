from django import template
from django.db.models import Count, F
from news.models import Category  # Импортируем модель Категории

register = template.Library()  # Регистрация Тега


@register.simple_tag()  # Декоратор. *Возможность изменить поведение функции.
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')  # Декоратор и рендер шаблона Лист_категории
def show_categories():
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    return {'categories': categories}
