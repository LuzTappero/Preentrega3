from django import forms

class ProductoFormulario(forms.Form):
    nombre=forms.CharField(max_length=250)
    descripcion= forms.CharField()
    precio= forms.CharField()

class BuscarProductoFormulario(forms.Form):
    nombre= forms.CharField(max_length=250)

class CrearUsuario(forms.Form):
    usuario= forms.CharField(max_length=255)
    email= forms.CharField(max_length=100)

class BuscarUsuario(forms.Form):
    usuario= forms.CharField(max_length=255)


