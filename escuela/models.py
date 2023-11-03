from django.db import models

# Create your models here.

class Escuela(models.Model):
    idEscuela = models.CharField(primary_key=True, max_length=100)
    nombreEscuela = models.CharField(max_length=100)
