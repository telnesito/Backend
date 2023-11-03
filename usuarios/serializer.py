from rest_framework import serializers
from .models import Usuarios, PerfilEstudiante

class UsuariosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuarios
        fields = '__all__'
        
class PerfilEstudianteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=PerfilEstudiante
        fields='__all__'