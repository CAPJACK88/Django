from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import login, logout
from .forms import UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


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
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Document.objects.filter(publications=True)


class CategoryList(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'doc/doc_list.html'
    context_object_name = 'doc'
    allow_empty = False
    queryset = Document.objects.select_related('Category')
    paginate_by = 10

    def get_queryset(self):
        return Document.objects.filter(category_id=self.kwargs['category_id'], publications=True)


class SearchTitle(ListView):
    model = Document
    template_name = 'doc/doc_list.html'
    context_object_name = 'doc'

    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Document.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = f"search={self.request.GET.get('search')}&"
        return context
