from django.urls import path 
from . import views 
urlpatterns = [
    path("",views.home),
    path("email",views.email),
    path("login",views.login),
    
]
