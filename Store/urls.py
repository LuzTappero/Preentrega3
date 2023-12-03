from django.urls import path
from django.http import HttpResponse

from Store.views import Store

app_name = 'Store'

urlpatterns = [
    path ('Store/', Store),
    ]
