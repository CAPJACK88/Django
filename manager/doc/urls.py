from django.urls import path
from .views import *

urlpatterns = [
    path('', plug, name='plug'),
    path('doc/', docList.as_view(), name='doc'),
]
