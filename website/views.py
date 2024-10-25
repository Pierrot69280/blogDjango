from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm, SignupForm, LoginForm
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

def article_create(request):
    if request.method == "POST":
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid():
            articleForm.save()
            return redirect('article_index')
    else:
        articleForm = ArticleForm()
    return render(request, "website/articles/create.html", {"articleForm": articleForm})


def article_edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == "POST":
        articleForm = ArticleForm(request.POST, instance=article)
        if articleForm.is_valid():
            articleForm.save()
            return redirect('article_index')
    else:
        articleForm = ArticleForm(instance=article)
    return render(request, "website/articles/edit.html", {"articleForm": articleForm})


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'website/registration/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('article_index')
    else:
        form = LoginForm()
    return render(request, 'website/registration/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
