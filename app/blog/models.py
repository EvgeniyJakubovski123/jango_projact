from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    image = models.URLField()  # ссылка на картинку
    publication_date = models.DateField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    guest_name = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField()
    publication_date = models.DateField(default=timezone.now)

    def __str__(self):
        name = self.author.username if self.author else self.guest_name
        return f"Comment by {name} on {self.article.title}"

