from django.urls import path
from .views import *

urlpatterns = [
    path('', plug, name='plug'),
    path('doc/', DocList.as_view(), name='doc'),
]
