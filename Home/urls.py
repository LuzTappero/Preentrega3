from django.urls import path


from Home.views import Home_view 
from Products.views import Products

app_name = 'Home'

urlpatterns = [
    path ('Home/', Home_view),
    path ('Home/Products', Products,)
    ]

