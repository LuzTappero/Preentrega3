from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProductoFormulario, BuscarProductoFormulario ,CrearComentarioFormulario, BuscarComentarioFormulario, CrearCategoriaProductoFromulario
from .models import Producto, Comentario, CategoriaProducto

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
                precio=informacion_limpia["precio"],
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


def crear_comentario(request):
    if request.method== "GET":
        context= {"form": CrearComentarioFormulario()}
        return render(request, 'Products/crear-comentario-formulario.html', context)
    elif request.method == "POST":
        formulario = CrearComentarioFormulario(request.POST)
        if formulario.is_valid():
            informacion_limpia= formulario.cleaned_data
            nuevo_comentario= Comentario(
                nombre = informacion_limpia["nombre"],
                edad = informacion_limpia["edad"],
                comentario= informacion_limpia["comentario"]
                )
            nuevo_comentario.save()
            return render(request, 'Products/products.html')
        else:
            context= {"form": formulario}
            return render(request,'Products/crear-comentario-formulario.html', context)


def buscar_comentario(request):
    if request.method == "GET":
        form = BuscarComentarioFormulario()
        return render(request, 
                     'Products/buscar_comentario_formulario.html',
                      context= {"form": form} 
                      )
    elif request.method == "POST":
        formulario = BuscarComentarioFormulario(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            comentarios_filtrados= Comentario.objects.filter(edad__icontains=informacion["edad"])
            context= {"comentarios": comentarios_filtrados}
            return render(request, 'Products/comentarios-list.html', context)
        
    else:
        return render (request, 'Products/comentarios-list.html', context={})


def crear_categoria_producto(request):
    if request.method == "GET":
        context= {"form": CrearCategoriaProductoFromulario()}
        return render(request, 'Products/crear-categorias-formulario.html', context)
    elif request.method == "POST":
        formulario= CrearCategoriaProductoFromulario(request.POST)
        if formulario.is_valid():
            informacion_limpia= formulario.cleaned_data
            nueva_categoria=CategoriaProducto(
                nombre= informacion_limpia["nombre"],
                descripcion= informacion_limpia["descripcion"]
            )
            nueva_categoria.save()
            return render (request,'Products/products.html')
        else:
            context= {"form": formulario}
            return render (request, 'Products/crear-categorias-formulario.html', context)



                







