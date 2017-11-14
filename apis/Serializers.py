from rest_framework import serializers
from .models import Modelos
from django.contrib.auth.models import User

class ModelosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Modelos
        fields = ('id', 'title', 'description', 'created','owner')
