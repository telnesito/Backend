from rest_framework import serializers
from .models import Publicacion, capitulosPublicacion

class PublicacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Publicacion
    fields = '__all__'


class VideosPublicacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = capitulosPublicacion
    fields = '__all__'