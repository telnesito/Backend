from rest_framework import serializers
from .models import Publicacion, capitulosPublicacion, Comentarios, cursosIniciados




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
    
class CursosIniciadosSerializer(serializers.ModelSerializer):
  class Meta:
    model = cursosIniciados
    fields = '__all__'