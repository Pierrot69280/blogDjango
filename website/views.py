from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

def article_index(request):
    articles = Article.objects.all()
    return render(request, 'website/articles/index.html', {'articles': articles})

def article_show(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'website/articles/show.html', {'article': article})


def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('article_index')