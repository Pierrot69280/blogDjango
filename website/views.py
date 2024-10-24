from django.shortcuts import render
from .models import Article

def article_index(request):
    articles = Article.objects.all()
    return render(request, 'website/articles/index.html', {'articles': articles})

def article_show(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'website/articles/show.html', {'article': article})

