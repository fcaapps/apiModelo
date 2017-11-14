from django.shortcuts import render
from .models import Produtos
from rest_framework import viewsets
from .Serializers import ProdutoSerializer
from django.contrib.auth.models import User

class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all().order_by('-created')
    serializer_class = ProdutoSerializer
