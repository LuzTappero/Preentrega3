from django.urls import path
from . import views


# app_name = 'Products'

urlpatterns = [
    path ('Products/', views.Products, name='Products'),
    path ('Products/crear/', views.crear_productos, name="crear_productos"), # type: ignore
    path ('Products/buscar/', views.buscar_productos , name="buscar_productos"),  # type: ignore
    path ('Products/crearUsuario/', views.crear_usuario, name="crearUsuario"), # type: ignore
]
