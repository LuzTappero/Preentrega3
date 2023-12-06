from django.db import models


class CategoriaProducto(models.Model):
    nombre= models.CharField(max_length=255, unique=True)
    descripcion= models.CharField(max_length=5000)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=2000)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nombre
    

class Comentario(models.Model):
    nombre= models.CharField(max_length=255)
    edad= models.IntegerField()
    comentario= models.TextField(max_length=1000)
    
    def __str__(self):
        return self.comentario
    
