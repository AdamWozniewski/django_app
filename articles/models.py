#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 150, verbose_name="Tytuł")
    content = models.TextField(verbose_name = "Zawartość")
    published = models.DateTimeField(verbose_name = "Data Publikacji")
    image = models.FileField(upload_to = "images/", verbose_name = "obrazek strony", null=True, blank=True)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    user = models.CharField(max_length = 150, verbose_name="Użytkownik")
    content = models.TextField(verbose_name="Zawartość komentarza")
    published = models.DateTimeField(verbose_name="Data Publikacji komentarza")
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return self.user