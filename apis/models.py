from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class Modelos(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='modelos', blank=True,null=True)

    def __str__(self):
        return "%s" % self.title
