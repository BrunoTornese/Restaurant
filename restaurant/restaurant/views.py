from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from forms import *
from models import *

def inicio(request): # vista de inicio
    return render(request, 'inicio.html')

def agregar_ingrediente(request): # vista de agregar ingrediente
    if request.method == 'POST': # si el metodo es post
        form = ingrediente_form(request.POST) # crea el formulario
        if form.is_valid(): # si el formulario es valido
            ingrediente = form.save(commit=False) # guarda el ingrediente
            ingrediente.save() # guarda el ingrediente
            return redirect('inicio.html', pk= ingrediente.recipe.pk) # redirecciona al inicio
    else: # si el metodo es get
        form = ingrediente_form()  # crea el formulario
    return render(request, 'agregar_ingrediente.html', {'form': form})# redirecciona a la pagina con el formulario en post

def crear_receta(request): # vista de crear receta
    if request.method == 'POST': # si el metodo es post
        form = receta_form(request.POST) # crea el formulario
        if form.is_valid(): # si el formulario es valido
            form.save() # guarda el receta
            return redirect('lista_recetas.html') # redirecciona al inicio
    else:
        form = receta_form() # crea el formulario
    return render(request,'crear_receta.html', {'form': form}) # redirecciona a crear receta con el formulario

def eliminar_ingrediente(request, ingrediente_nombre): # vista de eliminar ingrediente
    if request.method == 'POST': # si el metodo es post
        ingrediente = Ingrediente.objects.get(nombre=ingrediente_nombre) # obtiene el ingrediente
        ingrediente.delete() # elimina el ingrediente

        ingrediente= Ingrediente.objects.all() # obtiene todos los ingredientes
        return render(request, 'lista_ingredientes.html', {'ingredientes': ingrediente}) # retorna a la lista de ingredientes
    
def eliminar_receta(request, receta_nombre): # vista de eliminar receta
    if request.method == 'POST': # si el metodo es post
        receta = Receta.objects.get(nombre=receta_nombre) # obtiene el receta
        receta.delete() # elimina el receta

        receta = Receta.objects.all() # obtiene todos los recetas
        return render(request, 'lista_recetas.html', {'recetas': receta}) # redireciona a la lista de recetas
    
def editar_ingrediente(request, ingrediente_nombre): # vista de editar ingrediente
    ingrediente = Ingrediente.objects.get(nombre=ingrediente_nombre) # obtiene el ingrediente
    if request.method == 'POST': # si el metodo es post
        formulario = ingrediente_form(request.POST, instance=Ingrediente.objects.get(nombre=ingrediente_nombre)) #  crea el formulario 
        if formulario.is_valid(): # si el formulario es valido
            informacion = formulario.cleaned_data # limpia la data del formulario dejando lo importante
            ingrediente.set_nombre(informacion['nombre']) # obtiene el nombre del ingrediente
            ingrediente.set_precio(informacion['precio']) # obtiene el precio del ingrediente
            return render(request, 'agregar_ingrediente.html', {'form': formulario}) # retorna a la vista de agregar ingrediente
    else: # si el metodo es get
        formulario = ingrediente_form(instance=Ingrediente) # se crea el formulario
    return render(request, 'editar_ingrediente.html', {'formulario': formulario, 'ingrediente': ingrediente.Nombre}) # redirecciona a editar ingrediente 
        
def editar_receta(request, receta_nombre): # vista de editar receta 
    receta = Receta.objects.get(nombre=receta_nombre) # obtiene la receta
    if request.method == 'POST': # si el metodo es post
        formulario = receta_form(request.POST, instance=Receta.objects.get(nombre=receta_nombre)) #  crea el formulario 
        if formulario.is_valid(): # si el formulario es valido
            informacion = formulario.cleaned_data # limpia la data del formulario dejando
            receta.set_nombre(informacion['nombre']) # obtiene el nombre del receta
            receta.set_descripcion(informacion['descripcion']) # obtiene el descripcion del receta
            receta.set_ingredientes(informacion['ingredientes']) # obtiene los ingredientes
            return render(request, 'crear_receta.html', {'form': formulario}) # retorna a la vista de crear receta
    else: # si el metodo es get
        formulario = receta_form(instance=Receta) # se crea el formulario
    return render(request, 'editar_receta.html', {'formulario': formulario, 'receta': receta.nombre}) # redirecciona a editar receta