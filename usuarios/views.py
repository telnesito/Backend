from rest_framework import viewsets
from .serializer import UsuariosSerializer, PerfilEstudianteSerializer
from .models import Usuarios,PerfilEstudiante
# Create your views here.

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset=Usuarios.objects.all()
    serializer_class=UsuariosSerializer


class PerfilEstudianteViewSet(viewsets.ModelViewSet):
    queryset=PerfilEstudiante.objects.all()
    serializer_class=PerfilEstudianteSerializer