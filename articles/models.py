#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 150, verbose_name="Tytuł")
    content = models.TextField(verbose_name = "Zawartość")
    published = models.DateTimeField(verbose_name = "Data Publikacji")

    def __unicode__(self):
        return self.title