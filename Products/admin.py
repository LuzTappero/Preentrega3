from django.contrib import admin
from . import models

admin.site.register(models.Producto)
admin.site.register(models.Comentario)
admin.site.register(models.CategoriaProducto)
