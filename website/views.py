from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm, SignupForm, LoginForm, CommentForm
from .models import Article, Comment


def article_index(request):
    articles = Article.objects.all()
    return render(request, 'website/articles/index.html', {'articles': articles})


def article_show(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('article_show', article_id=article_id)
    else:
        comment_form = CommentForm()

    return render(request, 'website/articles/show.html', {
        'article': article,
        'comments': comments,
        'comment_form': comment_form
    })

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    article_id = comment.article.id
    if request.user == comment.author:
        comment.delete()
    return redirect('article_show', article_id=article_id)

def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article.author == request.user:
        article.delete()
    return redirect('article_index')

def article_create(request):
    if request.method == "POST":
        articleForm = ArticleForm(request.POST, request.FILES)
        if articleForm.is_valid():
            article = articleForm.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_index')
    else:
        articleForm = ArticleForm()
    return render(request, "website/articles/create.html", {"articleForm": articleForm})

def article_edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article.author != request.user:
        return redirect('article_index')

    if request.method == "POST":
        articleForm = ArticleForm(request.POST, request.FILES, instance=article)
        if articleForm.is_valid():
            articleForm.save()
            return redirect('article_index')
    else:
        articleForm = ArticleForm(instance=article)
    return render(request, "website/articles/edit.html", {"articleForm": articleForm, "article": article})

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
