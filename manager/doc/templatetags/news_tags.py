from django import template
from django.db.models import Count, F
from doc.models import Category

register = template.Library()


@register.inclusion_tag('include/_list_categories.html')
def show_categories():
    categories = Category.objects.annotate(cnt=Count('document', filter=F('document__publications'))).filter(cnt__gt=0)
    return {'categories': categories}
