from django.db import models
from usuarios.models import Usuarios
# Create your models here.

class Publicacion(models.Model):
  idPublicacion = models.AutoField(primary_key=True, unique=True)
  cedulaCreador = models.ForeignKey(Usuarios,to_field='cedula', on_delete=models.CASCADE ) 
  tituloPublicacion = models.CharField(max_length=100)
  descripcionPublicacion = models.TextField()
  tipoPublicacion = models.CharField(max_length=100)
  fechaPublicacion = models.DateTimeField(auto_created=True)

  def __str__(self):
    return self.tituloPublicacion


class capitulosPublicacion(models.Model):
  idVideoPublicacion = models.AutoField(primary_key=True)
  idPublicacion = models.ForeignKey(Publicacion, to_field='idPublicacion', on_delete=models.CASCADE)
  video_url = models.FileField(upload_to='capitulos/')
  tituloCapitulo = models.CharField(max_length=100)
  descripcionCapitulo = models.CharField(max_length=100)


