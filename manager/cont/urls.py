from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('search/', views.Search.as_view(), name='search'),
]