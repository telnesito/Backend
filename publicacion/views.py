from rest_framework import viewsets
from .serializer import PublicacionSerializer, VideosPublicacionSerializer
from .models import Publicacion, capitulosPublicacion

# Create your views here.

class PublicacionViewSet(viewsets.ModelViewSet):
  queryset = Publicacion.objects.all()
  serializer_class = PublicacionSerializer

class VideosPublicacionViewSet(viewsets.ModelViewSet):
  queryset = capitulosPublicacion.objects.all()
  serializer_class = VideosPublicacionSerializer