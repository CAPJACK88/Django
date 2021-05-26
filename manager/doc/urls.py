from django.urls import path
from .views import *

urlpatterns = [
    path('', UserLogin, name='UserLogin'),
    path('doc/', DocList.as_view(), name='DocList'),
    path('category/<int:category_id>/', CategoryList.as_view(), name='CategoryList'),
]
