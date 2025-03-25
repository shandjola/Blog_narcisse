# Narcise/models.py
from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=200)
    cathegorie = models.CharField(max_length=20,default='science')
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)  #via pillow pour la gestion des image 

    def __str__(self):
        return self.titre