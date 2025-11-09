from django.contrib import admin
from .models import Category, Tag, Article, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "icon")
    search_fields = ("title",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "publication_date", "is_published")
    list_filter = ("category", "is_published", "publication_date")
    search_fields = ("title", "author", "text")
    filter_horizontal = ("tag",)
    date_hierarchy = "publication_date"
    ordering = ("-publication_date",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "article", "publication_date")
    search_fields = ("author", "text")
    list_filter = ("publication_date",)
