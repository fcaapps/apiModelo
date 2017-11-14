from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class Produtos(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    price=models.CharField(max_length=10)
    cost=models.CharField(max_length=10, blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='produtos', blank=True,null=True)

    def __str__(self):
        return "%s" % self.title
