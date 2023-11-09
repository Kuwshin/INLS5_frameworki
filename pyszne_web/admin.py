from django.contrib import admin
from .models import Article


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'year', 'content', 'author', 'category', 'image']
    list_display = ('title', 'year', 'author', 'category')
    list_filter = ('author', 'category', 'year')
    search_fields = ('title', 'content')

