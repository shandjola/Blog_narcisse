# Narcise/urls.py
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
    path('voire_plus/', views.voire_plus , name='voire_plus'),
    path('article/<int:id>/', views.detail_article, name='detail_article'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)