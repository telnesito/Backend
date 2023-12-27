from rest_framework import viewsets
from .serializer import PublicacionSerializer, VideosPublicacionSerializer, ComentariosPublicacionSerializer
from .models import Publicacion, capitulosPublicacion, Comentarios

# Create your views here.

class PublicacionViewSet(viewsets.ModelViewSet):
  queryset = Publicacion.objects.all()
  serializer_class = PublicacionSerializer

class VideosPublicacionViewSet(viewsets.ModelViewSet):
  queryset = capitulosPublicacion.objects.all()
  serializer_class = VideosPublicacionSerializer

class ComentariosViewSet(viewsets.ModelViewSet):
  queryset = Comentarios.objects.all()
  serializer_class = ComentariosPublicacionSerializer