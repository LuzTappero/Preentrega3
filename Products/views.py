from django.shortcuts import render

def Products (request):
    return render(request, 'Products/products.html')