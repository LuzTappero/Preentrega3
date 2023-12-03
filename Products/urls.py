from django.urls import path
from django.http import HttpResponse

from Products.views import Products

app_name = 'Products'

urlpatterns = [
    path ('Products/', Products, ),
    ]
