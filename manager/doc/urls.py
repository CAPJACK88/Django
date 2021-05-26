from django.urls import path
from .views import *

urlpatterns = [
    path('', user_login, name='user_login'),
    path('logout/', user_logout, name='logout'),
    path('doc/', DocList.as_view(), name='DocList'),
    path('category/<int:category_id>/', CategoryList.as_view(), name='CategoryList'),
]
