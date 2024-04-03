from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('<str:slug>/', RecordsByCategoryView.as_view(), name='records-by-category'),
]