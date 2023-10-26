# views.py
from django.shortcuts import render
from .models import Article

def articles(request):
    all_articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': all_articles})

# articles.html

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")