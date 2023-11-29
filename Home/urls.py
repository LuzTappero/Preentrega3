from django.urls import path
from django.http import HttpResponse

from Home.views import Home

app_name = 'Home'

urlpatterns = [
    path ('Home/', Home),
    ]

