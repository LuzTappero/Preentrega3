from django.urls import path
from . import views


# app_name = 'Products'

urlpatterns = [
    path ('Products/', views.Products, name='Products'),
    path ('Products/crear/', views.crear_productos, name="crear_productos"), # type: ignore
    path ('Products/buscar/', views.buscar_productos , name="buscar_productos"),  # type: ignore
    path ('Products/crearComentario/', views.crear_comentario , name= "crear_comentario"),# type: ignore
    path ('Products/buscarComentario/', views.buscar_comentario, name="buscar_comentario"),# type: ignore
    path ('Products/crearCategorias/', views.crear_categoria_producto, name="crear_categoria"), #type: ignore
]
