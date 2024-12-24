from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    # Puedes agregar campos adicionales si es necesario
    pass

class Lugar(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    direccion = models.CharField(max_length=255)
    latitud = models.FloatField()
    longitud = models.FloatField()
    url_mapa = models.URLField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)  # Valor predeterminado


    def __str__(self):
        return self.nombre
