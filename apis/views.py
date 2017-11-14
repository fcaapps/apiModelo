from django.shortcuts import render
from .models import Modelos
from rest_framework import viewsets
from .Serializers import ModelosSerializer
from django.contrib.auth.models import User

class ModelosViewSet(viewsets.ModelViewSet):
    queryset = Modelos.objects.all().order_by('-created')
    serializer_class = ModelosSerializer
