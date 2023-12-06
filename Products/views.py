from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProductoFormulario, BuscarProductoFormulario , CrearUsuario, BuscarUsuario
from .models import Producto, User






def Products (request):
    return render(request, 'Products/products.html')

def crear_productos(request):
    if request.method == "GET":
        context= {"form": ProductoFormulario()}
        return render(request, 'Products/formulario-crear-producto.html', context)
    else:
        print (request.POST)
        formulario= ProductoFormulario(request.POST)
        if formulario.is_valid():
            informacion_limpia= formulario.cleaned_data
            modelo= Producto(
                nombre=informacion_limpia["nombre"], 
                descripcion=informacion_limpia["descripcion"], 
                precio=informacion_limpia["precio"]
                )
            modelo.save()
            return render(request, 'Products/products.html')

def buscar_productos(request):
    if request.method == "GET":
        form = BuscarProductoFormulario()
        return render( 
            request,
            'Products/busqueda-producto-formulario.html',
            context={"form": form}
        )
    elif request.method == "POST":
        formulario = BuscarProductoFormulario(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            productos_filtrados = Producto.objects.filter(nombre__icontains=informacion["nombre"])
            context= {"productos": productos_filtrados}
            return render (request, 'Products/productos_list.html', context)
        
    else:
        return render (request, 'Products/productos_list.html', context={})

def crear_usuario(request):
    if request.method == "GET":
        context={"form": CrearUsuario}
        return render(request, 'Products/crear_usuario.html', context)
    elif request.method == "POST":
        formulario= CrearUsuario(request.POST)
        if formulario.is_valid():
            informacion_limpia= formulario.cleaned_data
            usuario= informacion_limpia["usuario"]
            email=informacion_limpia["email"]
             #crea un nuevo usuario
            user= User.objects.create_user(email=email, username=usuario,)
            return render(request, 'Home/Home.html')
        







