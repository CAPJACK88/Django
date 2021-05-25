from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Document, Category, User
from django.http import HttpResponse


def plug(request):
    return HttpResponse('Заглущка / plug')


class DocList(ListView):
    model = Document
    template_name = 'doc/docList.html'
    context_object_name = 'doc'
