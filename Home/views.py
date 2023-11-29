from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def Home(request):
#     return render (request, "Home/templates/index.html")

# def Home(xx):
#     return HttpResponse("Welcome!")

def Home (xx):
    return render(xx, 'Home/index.html')



