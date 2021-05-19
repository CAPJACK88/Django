from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):  # Отображаем только опубликованные новости
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False  # Заперщаем показ пустых списков (страниц)

    def get_queryset(self):  # Отображаем только опубликованные новости и новости соответствующей категории
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category') # .select_related('category') - оптимизатор SQL запроса


class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    # template_name = 'news/news_detail.html'
    context_object_name = 'news_item'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add-news.html'

# def index(request):  # Рендер шаблона Индекс
#     news = News.objects.all()  # Импортируем объекты из db News
#     # categories = Category.objects.all()  # Импортируем все объекты из db Category
#     context = {  # Словарь с ключами
#         'news': news,
#         'title_news': 'Список новостей',
#         'title_category': 'Категории',
#         # 'categories': categories,
#     }
#     return render(request, template_name='news/index.html', context=context)  # Возвращаем рендер


# def get_category(request, category_id):
#     category = get_object_or_404(Category, pk=category_id)  # Обработчик страниц с кодом ошибки 404
#     news = News.objects.filter(category_id=category_id)
#     # category = Category.objects.get(pk=category_id)
#     # categories = Category.objects.all() # Взамен используем кастомный тег для получения списка категорий
#     context = {
#         'news': news,
#         'title_news': 'Список новостей',
#         'title_category': 'Категории',
#         'category': category,
#         # 'categories': categories,
#     }
#     return render(request, template_name='news/category.html', context=context)


# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     context = {
#         'news_item': news_item,
#     }
#     return render(request, template_name='news/view_news.html', context=context)

#
# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'news/add-news.html', context=context)
