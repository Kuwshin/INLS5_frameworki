# views.py
from django.shortcuts import render
from .models import Article

def articles(request):
    all_articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': all_articles})
