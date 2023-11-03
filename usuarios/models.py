from django.db import models

# Create your models here.


class Usuarios(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    correo_electronico = models.CharField(max_length=244, unique=True)
    nombre = models.CharField(max_length=244)
    apellido = models.CharField(max_length=244)
    usuario = models.CharField(max_length=244)
    rol = models.CharField(max_length=100)
    foto = models.CharField(max_length=244)
    
    def __str__(self):
        return self.correo_electronico
    

    