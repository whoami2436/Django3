from django.contrib import admin
from .models import Article, Comment

# Register your models here.


# admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author"]
    list_display_links = ["title", "author"]
    list_filter = ["created_date"]
    search_fields = ["title"]

    class Meta:
        model = Article


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ["comment_date"]
    search_fields = ["comment_author"]

    class Meta:
        model = Comment