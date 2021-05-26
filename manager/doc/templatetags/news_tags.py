from django import template
from django.db.models import Count, F
from doc.models import Category  # Импортируем модель Категории

register = template.Library()  # Регистрация Тега


@register.inclusion_tag('include/_list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories,}

# categories = Category.objects.annotate(cnt=Count('CategoryList', filter=F('DocList__publications'))).filter(cnt__gt=0)
