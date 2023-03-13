from django.db import models

class Ingrediente(models.Model):
    Nombre = models.CharField(max_length=100) # nombre del ingrediente
    Precio = models.IntegerField(max_digits=10) # precio del ingrediente

class Receta(models.Model):
    nombre = models.CharField(max_length=100) # nombre de la receta
    descripcion = models.CharField(max_length=100) # descripcion de la receta
    ingredientes = models.ManyToManyField(Ingrediente) # ingredientes de la receta
    
    def __str__(self):
        return self.nombre + " " + self.descripcion + " " + self.ingredientes.all()
    
# Usando el Many-to-Many en este caso, el campo ingredientes en el modelo Receta es un ManyToManyField que apunta al modelo Ingrediente.
# Esto permitirá que cada receta tenga varios ingredientes y cada ingrediente pueda estar presente en varias recetas

