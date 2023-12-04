from django.urls import path
from . import views

# app_name = 'Store'

urlpatterns = [
    path ('Store/', views.Store, name='Store'),
    ]
