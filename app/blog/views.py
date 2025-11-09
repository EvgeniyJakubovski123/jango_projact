from django.shortcuts import render, get_object_or_404
from .models import Article,Category

def home(request):
    latest_articles = Article.objects.all().order_by('-publication_date')[:3]
    return render(request, 'blog/home.html', {'latest_articles': latest_articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comment_set.all().order_by('publication_date')  # по дате по возрастанию
    return render(request, 'blog/article_detail.html', {
        'article': article,
        'comments': comments
    })
def all_articles(request):
    articles = Article.objects.filter(is_published=True).order_by('-publication_date')
    return render(request, 'blog/all_articles.html', {'articles': articles})

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories_list.html', {'categories': categories})