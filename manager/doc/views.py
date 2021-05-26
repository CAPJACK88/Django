from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import login, logout
from .forms import UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


def UserLogin(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('DocList')
    else:
        form = UserLoginForm()
    return render(request, template_name='doc/login_user.html', context={"form": form})


class DocList(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'doc/doc_list.html'
    context_object_name = 'DocList'
    allow_empty = False


class CategoryList(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'doc/doc_list.html'
    context_object_name = 'CategoryList'
    allow_empty = False

    def get_queryset(self):
        return Document.objects.filter(category_id=self.kwargs['category_id'], publications=True).select_related(
            'category')
