from django.shortcuts import render
from django.http import HttpResponse

def Products (request):
    return render(request, 'Products/products.html')