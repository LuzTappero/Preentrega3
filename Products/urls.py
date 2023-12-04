from django.urls import path, include
# from django.http import HttpResponse
from . import views

# app_name = 'Products'

urlpatterns = [
    path ('Products/', views.Products, name='Products'),
    ]
