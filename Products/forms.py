from django import forms
from .models import  Comentario, Producto, CategoriaProducto

class ProductoFormulario(forms.Form):
    nombre=forms.CharField(max_length=250)
    descripcion= forms.CharField()
    precio= forms.CharField()
    categoria= forms.CharField()

class BuscarProductoFormulario(forms.Form):
    nombre= forms.CharField(max_length=250)

class CrearComentarioFormulario(forms.Form):
    nombre= forms.CharField(max_length=255)
    edad= forms.IntegerField(max_value=120)
    comentario= forms.CharField(max_length=10000)

class BuscarComentarioFormulario(forms.Form):
    edad= forms.IntegerField(max_value=120)

class CrearCategoriaProductoFromulario(forms.Form):
     nombre= forms.CharField(max_length=255)
     descripcion= forms.CharField(max_length=5000)





