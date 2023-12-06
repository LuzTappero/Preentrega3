from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
   
    def __str__(self):
        return self.nombre
    

class User(models.Model):
    usuario= models.CharField(max_length=255, unique=True)
    email= models.CharField(max_length=100)

    def __str__(self):
        return self.usuario
    

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.item