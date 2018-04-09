#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Notifications(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'tytuł wiadomości')
    content = models.TextField(verbose_name = 'Treść wiadomosci')
    viewed = models.BooleanField(default = False, verbose_name = 'Otwarta')
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

@receiver(post_save, sender = User)
def send_welcome_message(sender, **kwargs):
    if kwargs.get('created', False):
        Notifications.objects.create(user = kwargs.get('instance'),
                                     title = "Witaj",
                                     content = "Treść powitalna"
                                     )