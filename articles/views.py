from django.shortcuts import (
    render, redirect, get_list_or_404,
    get_object_or_404
)
from django.utils.text import slugify

from articles.models import Article
from articles.forms import ArticleForm


def articles_list(request):
    articles = get_list_or_404(Article)
    return render(request, 'articles/articles_list.html', {'articles': articles})


def articles_new(request):

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            topic = form.cleaned_data['topic']
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            article.topic = topic
            article.title = title
            article.slug = slugify(title)
            article.content = content
            article.save()
        
        return redirect('articles:list')

    else:
        form = ArticleForm()

    return render(request, 'articles/articles_new.html', {'form': form})


def articles_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles/articles_detail.html', {'article': article})


def articles_update(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.slug = slugify(article.title)
            form.save()

            return redirect('articles:list')

    else:
        form = ArticleForm(instance=article)
        return render(request, "articles/articles_new.html", {'form': form})


def articles_delete(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.delete()
    return redirect('articles:list')
