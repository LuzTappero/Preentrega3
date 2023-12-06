from django.contrib import admin
from . import models

admin.site.register(models.Producto)
admin.site.register(models.User)
admin.site.register(models.Carrito)
