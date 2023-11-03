
# Importacionnes
from django.db import models
from escuela.models import Escuela


# Se crean los modelos

""" 
    Al agregar un modelo es como si estuviesemos creando una tabla en la base de datos.
    Aqui solo iran los modelos que esten relacionados al control de usuarios, como la tabla usuarios y los perfiles
"""

class Usuarios(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True, unique=True)
    correo_electronico = models.CharField(max_length=244, unique=True)
    nombre = models.CharField(max_length=244)
    apellido = models.CharField(max_length=244)
    usuario = models.CharField(max_length=244)
    rol = models.CharField(max_length=100)
    foto = models.CharField(max_length=244)
    
    def __str__(self):
        return self.correo_electronico
    
class PerfilEstudiante (models.Model):
    idPerfilEstudiante = models.CharField(primary_key=True)
    cedulaEstudiante = models.ForeignKey(Usuarios, to_field='cedula', on_delete=models.CASCADE, unique=True)
    semestreEstudiante = models.CharField(max_length=100)
    escuelaEstudiante = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cedulaEstudiante