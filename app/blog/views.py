from django.shortcuts import render, get_object_or_404
from .models import Article

def home(request):
    latest_articles = Article.objects.filter(is_published=True).order_by('-publication_date')[:3]
    return render(request, 'blog/home.html', {'latest_articles': latest_articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})
