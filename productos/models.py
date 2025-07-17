from django.db import models

# Create your models here.

class Sarten(models.Model):
    marca = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    fecha = models.DateField()
    
    def __str__(self):
        return f'ID: {self.id} - Marca: {self.marca}'