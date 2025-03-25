# Narcise/views.py
from django.shortcuts import render, get_object_or_404
from .models import Article
from django.utils import timezone
from datetime import timedelta

def liste_articles(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

def voire_plus(request):
   # Date limite pour considérer un article comme "ancien"
    limit_date = timezone.now() - timedelta(weeks=2)

    # Articles anciens (plus de 2 semaines)
    old_articles = Article.objects.filter(created_at__lt=limit_date)

    return render(request, 'detail.html', {
        'old_articles': old_articles,
    })

def detail_article(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'detail.html', {'article': article})
