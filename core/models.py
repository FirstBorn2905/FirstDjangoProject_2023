from typing import Any
from django.db import models

# Create your models here.
class Personal (models.Model):
    #IMPLEMENTACIÓN DE IMAGENES
    # 
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    apellido = models.CharField(max_length=20, verbose_name='Apellido')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    telefono = models.IntegerField(verbose_name='Telefono')
    OPCIONES_AREAS =[
        ('Servicio', 'Servicio'),
        ('Cocina', 'Cocina'),
        ('Motorizados', 'Motorizados')
    ]
    areas = models.CharField(max_length=12, verbose_name='Areas', choices=OPCIONES_AREAS, default=None)
    
    def __str__(self):
        fila = self.nombre + " " + self.apellido
        return fila
    
    #FUNCIÓN DE ELIMINACIÓN DE IMAGEN DE LA CARPETA
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        
class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Personal, null=False, blank=False, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=20)
    producto = models.CharField(max_length=20)
    cantidad = models.PositiveIntegerField()
    fechaPeticion = models.DateTimeField(auto_now_add=True)
    
    def delete(self, using=None, keep_parents=False):
        super().delete()
    
class ReporteVentas(models.Model):
    id = models.AutoField(primary_key=True)
    ganancia = models.PositiveIntegerField()
    perdida = models.PositiveIntegerField()
    date = models.DateTimeField(null=True, auto_now_add=True)
    
    def __str__(self):
        return f'{self.date}  id:{self.id}'