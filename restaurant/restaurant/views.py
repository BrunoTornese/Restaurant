from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from forms import *
from models import *

def inicio(request): # vista de inicio
    ingredientes = Ingrediente.objects.all() # creo una variable que obtenga todos los objetos ingredientes
    recetas = Receta.objects.all() # creo una variable que obtenga todos los objetos recetas
    sub_recetas = sub_receta.objects.all()# creo una variable que obtenga todos los objetos sub recetas
    return render(request, 'inicio.html',{'ingredientes': ingredientes}, {'recetas': recetas},{'sub recetas': sub_recetas}) # retorna a la vista de inicio

@login_required 
def agregar_ingrediente(request): # vista de agregar ingrediente
    if request.method == 'POST': # si el metodo es post
        form = ingrediente_form(request.POST) # crea el formulario
        if form.is_valid(): # si el formulario es valido
            ingrediente = form.save(commit=False) # guarda el ingrediente en una variable
            ingrediente.save() # guarda el ingrediente
            return redirect('inicio.html') # redirecciona al inicio
    else: # si el metodo es get
        form = ingrediente_form(request.POST)  # crea el formulario
    return render(request, 'agregar_ingrediente.html', {'form': form})# redirecciona a la pagina con el formulario en post

@login_required
def crear_sub_receta(request): # vista para agregar una subreceta
    if request.method == 'POST': # si el metodo es post
        form = sub_receta_form(request.POST) # crea el formulario
        if form.is_valid(): # si el formulario es valido
            sub_receta = form.save(commit=False) # guardar la subreceta en una variable
            sub_receta.save() # guardar la subreceta 
            return redirect('inicio.html') # retorna a la vista de inicio
        else: # si el metodo no es post
            form = sub_receta_form(request.POST) # crea el formulario con los  valores del post
        return render(request, 'agregar_sub_receta.html',{'form': form}) # retorna a la vista de agregar receta
    
@login_required 
def crear_receta(request): # vista de crear receta
    if request.method == 'POST': # si el metodo es post
        form = receta_form(request.POST) # crea el formulario
        if form.is_valid(): # si el formulario es valido
            form.save() # guarda el receta
            return redirect('inicio.html') # redirecciona al inicio
    else: # si el metodo no es post
        form = receta_form() # crea el formulario
    return render(request,'crear_receta.html', {'form': form}) # redirecciona a crear receta con el formulario

@login_required 
def eliminar_ingrediente(request, ingrediente_nombre): # vista de eliminar ingrediente
    if request.method == 'POST': # si el metodo es post
        ingrediente = Ingrediente.objects.get(nombre=ingrediente_nombre) # obtiene el ingrediente
        ingrediente.delete() # elimina el ingrediente

        ingrediente= Ingrediente.objects.all() # obtiene todos los ingredientes
        return render(request, 'lista_ingredientes.html', {'ingredientes': ingrediente}) # retorna a la lista de ingredientes

@login_required     
def eliminar_receta(request, receta_nombre): # vista de eliminar receta
    if request.method == 'POST': # si el metodo es post
        receta = Receta.objects.get(nombre = receta_nombre) # obtiene el receta
        receta.delete() # elimina el receta
        receta = Receta.objects.all() # obtiene todos los recetas
        return render(request, 'lista_recetas.html', {'recetas': receta}) # redireciona a la lista de recetas

@login_required
def eliminar_sub_recetas(request, sub_receta_nombre):# vista para eliminar subrecetas
    if request.method == 'POST': # si el metodo es post
        sub_receta = sub_receta.objects.get(nombre = sub_receta_nombre) # obtiene la subreceta
        sub_receta.delete() # elimina la receta
        sub_receta = sub_receta.objects.all() # obtiene todas las subrecetas
        return render(request, 'inicio.html', {'sub_recetas': sub_receta}) # redireciona a la lista de subrecetas
    
@login_required 
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

@login_required       
def editar_receta(request, receta_nombre): # vista de editar receta 
    receta = Receta.objects.get(nombre=receta_nombre) # obtiene la receta
    if request.method == 'POST': # si el metodo es post
        formulario = receta_form(request.POST, instance=Receta.objects.get(nombre=receta_nombre)) #  crea el formulario 
        if formulario.is_valid(): # si el formulario es valido
            informacion = formulario.cleaned_data # limpia la data del formulario 
            receta.set_nombre(informacion['nombre']) # obtiene el nombre del receta
            receta.set_descripcion(informacion['descripcion']) # obtiene el descripcion del receta
            receta.set_ingredientes(informacion['ingredientes']) # obtiene los ingredientes
            return render(request, 'crear_receta.html', {'form': formulario}) # retorna a la vista de crear receta
    else: # si el metodo es get
        formulario = receta_form(instance=Receta) # se crea el formulario
    return render(request, 'inicio.html', {'formulario': formulario, 'receta': receta.nombre}) # redirecciona a el inicio con la receta modificada

@login_required
def editar_sub_receta(request,sub_receta_nombre): # vista para editar subreceta
    sub_receta = sub_receta.objects.get(nombre = sub_receta_nombre) # obtiene la subreceta 
    if request.method == 'POST': # si el metodo es post
        formulario = ediar_sub_receta_form(request.POST, instance = Receta.objects.get(nombre = sub_receta_nombre)) # obtiene la subreceta a editar
        if formulario.is_valid(): # si el formulario es valido
            info = formulario.cleaned_data # limpia la data del formulario
            sub_receta.set_nombre(info['nombre']) # obtiene el nombre de la subreceta
            sub_receta.set_descripcion(info['descripcion']) # obtiene el descripcion
            sub_receta.set_ingredientes(info['ingredientes']) # obtiene los ingredientes
            return render(request, 'inicio.html', {'form': formulario, 'receta': sub_receta}) # redirecciona a el inicio con la subreceta modificada


def crear_usuario(request): # vista de crear usuario
    if request.method == 'POST': # si el metodo es post
        formulario = Usuario_form(request.POST) # crea el formulario
        if formulario.is_valid(): # si el formulario es valido
            formulario.save() # guarda el usuario
            return render('inicio.html') # redirecciona al inicio
    else: # si el metodo es get
        return render(request, 'crear_usuario.html', {'formulario': Usuario_form()}) # redirecciona a crear usuario con el formulario


