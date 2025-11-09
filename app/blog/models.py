from django.db import models


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
    author = models.CharField(max_length=100)
    text = models.TextField()
    image = models.URLField()  # ссылка на картинку
    publication_date = models.DateField()
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author} on {self.article.title}"

