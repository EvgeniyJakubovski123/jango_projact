from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('articles/', views.all_articles, name='all_articles'),
    path('categories/', views.categories_list, name='categories_list'),
]
