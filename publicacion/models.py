from django.db import models
from usuarios.models import Usuarios
# Create your models here.

class Publicacion(models.Model):
  idPublicacion = models.AutoField(primary_key=True)
  cedulaCreador = models.OneToOneField(Usuarios,to_field='cedula', on_delete=models.CASCADE ) 
  tituloPublicacion = models.CharField(max_length=100)
  descripcionPublicacion = models.TextField()
  tipoPublicacion = models.CharField(max_length=100)
  fechaPublicacion = models.DateTimeField(auto_created=True)

  def __str__(self):
    return self.tituloPublicacion
