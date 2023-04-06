from django.db import models
from django.contrib.auth.models import User

class Colectivos(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    hora_salida = models.TimeField()
    hora_llegada = models.TimeField()
    dias_de_circulacion = models.CharField(max_length=100)
    compania = models.CharField(max_length=100)
    precio = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.origen} a {self.destino}'