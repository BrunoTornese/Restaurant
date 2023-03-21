"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', inicio, name= 'inicio'),
    path('agregar_ingredientes/', agregar_ingrediente, name= 'agregar_ingrediente'),
    path('crear_sub_receta/', crear_sub_receta, name= 'crear_sub_receta'),
    path('crear_receta/', crear_receta, name= 'crear_receta'),
    path('eliminar_ingrediente/', eliminar_ingrediente, name='eliminar_ingrediente'),
    path('eliminar_receta/', eliminar_receta, name='eliminar_receta'),
    path('eliminar_sub_receta/', eliminar_sub_recetas, name = 'eliminar_sub_receta'),
    path('editar_ingrediente/', editar_ingrediente, name = 'editar_sub_ingrediente'),
    path('editar_receta/', editar_receta, name = 'editar_receta'),
    path('editar_sub_receta/', editar_sub_receta, name = 'editar_sub_receta'),   
]
