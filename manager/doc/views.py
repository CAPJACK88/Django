from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import login, logout
from .forms import UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
import json


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('DocList')
    else:
        form = UserLoginForm()
    return render(request, template_name='doc/login_user.html', context={"form": form})


def user_logout(request):
    logout(request)
    return redirect('user_login')


class DocList(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'doc/doc_list.html'
    context_object_name = 'doc'
    allow_empty = False
    queryset = Document.objects.select_related('Category')
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['qs_json'] = json.dumps(list(Document.objects.values()))
        return context

    def get_queryset(self):
        return Document.objects.filter(publications=True)


class CategoryList(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'doc/doc_list.html'
    context_object_name = 'doc'
    allow_empty = False
    queryset = Document.objects.select_related('Category')
    paginate_by = 3

    def get_queryset(self):
        return Document.objects.filter(category_id=self.kwargs['category_id'], publications=True)

# def index(request):
# search_query = self.request.GET.get('search')
#         # if search_query:
#         #     posts = Document.objects.filter(title__icontains=search_query)
#         #     context['posts'] = posts
#         # else:
#         #     posts = Document.objects.all()
#         #     context['posts'] = posts
