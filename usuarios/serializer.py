from rest_framework import serializers
from .models import Usuarios, PerfilEstudiante, PerfilProfesor, PerfilCoordinador

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
        fields='__all__'

class PerfilCoordinadorSerializer(serializers.ModelSerializer):

    class Meta:
        mode=PerfilCoordinador
        fields='__all__'
