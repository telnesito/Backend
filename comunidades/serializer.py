from rest_framework import serializers
from .models import Comunidades

class ComunidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comunidades
        fields='__all__'