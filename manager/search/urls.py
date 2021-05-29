from search import views
from django.urls import path

urlpatterns = [
    path('', views.show_list, name='show_list')
]
