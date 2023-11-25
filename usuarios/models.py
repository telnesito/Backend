
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
    correo_electronico = models.EmailField(max_length=254)
    nombre = models.CharField(max_length=244)
    apellido = models.CharField(max_length=244)
    usuario = models.CharField(max_length=244)
    rol = models.CharField(max_length=100)
    foto = models.ImageField()
    
    def __str__(self):
        return self.correo_electronico
    
class PerfilEstudiante (models.Model):
    idPerfilEstudiante = models.AutoField(primary_key=True)
    cedulaEstudiante = models.OneToOneField(Usuarios, to_field='cedula', on_delete=models.CASCADE,)
    semestreEstudiante = models.CharField(max_length=100)
    escuelaEstudiante = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cedulaEstudiante

class PerfilProfesor (models.Model):
    idPerfilProfesor = models.AutoField(primary_key=True)
    cedulaProfesor = models.OneToOneField(Usuarios,  on_delete=models.CASCADE)
    experienciaProfesor = models.CharField(max_length=244)
    materiaProfesor = models.CharField(max_length=244)
    fraseProfesor = models.CharField(max_length=244)
    sobreProfesor = models.CharField(max_length=244)
    
    def __str__(self):
        return self.cedulaProfesor
    
class PerfilCoordinador (models.Model):
    idPerfilCoordinador = models.AutoField(primary_key=True)
    cedulaCoordinador = models.OneToOneField(Usuarios,  on_delete=models.CASCADE)
    experienciaCoordinador = models.CharField(max_length=244)
    materiaCoordinador = models.CharField(max_length=244)
    fraseCoordinador = models.CharField(max_length=244)
    sobreCoordinador = models.CharField(max_length=244)
    