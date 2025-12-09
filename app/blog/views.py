from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def home(request):
    latest_articles = Article.objects.filter(is_published=True).order_by('-publication_date')[:3]
    return render(request, 'blog/home.html', {'latest_articles': latest_articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comments.all().order_by('publication_date')

    if request.method == 'POST':
        form = CommentForm(request.POST, user=request.user)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            if request.user.is_authenticated:
                comment.author = request.user
            comment.publication_date = timezone.now()
            comment.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = CommentForm(user=request.user)

    return render(request, 'blog/article_detail.html', {
        'article': article,
        'comments': comments,
        'form': form,
    })


def all_articles(request):
    articles = Article.objects.filter(is_published=True).order_by('-publication_date')
    return render(request, 'blog/all_articles.html', {'articles': articles})


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories_list.html', {'categories': categories})


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author != request.user:
        return redirect('article_detail', article_id=comment.article.id)
    form = CommentForm(request.POST or None, instance=comment, user=request.user)
    if form.is_valid():
        form.save()
        return redirect('article_detail', article_id=comment.article.id)
    return render(request, 'blog/edit_comment.html', {'form': form})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author == request.user or request.user.has_perm('blog.delete_comment'):
        comment.delete()
    return redirect('article_detail', article_id=comment.article.id)
