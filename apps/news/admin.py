from django.contrib import admin
from .models import Article, Comment
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'is_publicate')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'nick', 'text', 'date')