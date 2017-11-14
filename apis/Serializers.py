from rest_framework import serializers
from .models import Produtos
from django.contrib.auth.models import User

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produtos
        fields = ('id', 'title', 'description', 'status', 'cost', 'price', 'created','owner')
