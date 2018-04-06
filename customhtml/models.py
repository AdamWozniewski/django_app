#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class CustomHtml(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Tytuł')
    sourceHtml = models.TextField(verbose_name = 'Zawartość html')

    def __unicode__(self):
        return self.title