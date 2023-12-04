from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    categoria = models.CharField(max_length=50, choices=[('cafe', 'Café'), ('pasteleria', 'Pastelería')])

