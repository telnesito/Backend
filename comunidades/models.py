from django.db import models
from usuarios.models import Usuarios
# Create your models here.

class Comunidades(models.Model):
  idComunidad = models.AutoField(primary_key=True)
  cedulaCreador =  models.OneToOneField(Usuarios, to_field='cedula', on_delete=models.CASCADE,)
  nombreComunidad = models.CharField(max_length=144)
  descripcionComunidad = models.TextField()
  fechaCreada = models.DateTimeField(auto_created=True)
  