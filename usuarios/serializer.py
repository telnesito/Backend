from rest_framework import serializers
from .models import Usuarios, PerfilEstudiante, PerfilProfesor

class UsuariosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuarios
        fields = '__all__'
        
class PerfilEstudianteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=PerfilEstudiante
        fields='__all__'
        
class PerfilProfesorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=PerfilProfesor
        fiels='__all__'