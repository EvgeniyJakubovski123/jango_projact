from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.all_articles, name='all_articles'),
    path('categories/', views.categories_list, name='categories_list'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('comment/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
