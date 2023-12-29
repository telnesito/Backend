from rest_framework import serializers
from .models import Publicacion, capitulosPublicacion, Comentarios




class PublicacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Publicacion
    fields = '__all__'


class VideosPublicacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = capitulosPublicacion
    fields = '__all__'

class ComentariosPublicacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comentarios
    fields = '__all__'