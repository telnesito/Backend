from rest_framework import viewsets
from .serializer import ComunidadesSerializer
from .models import Comunidades
# Create your views here.

class ComunidadViewSet(viewsets.ModelViewSet):
  queryset = Comunidades.objects.all()
  serializer_class = ComunidadesSerializer