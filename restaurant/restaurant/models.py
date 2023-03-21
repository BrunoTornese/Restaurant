from django.db import models

class Ingrediente(models.Model):
    Nombre = models.CharField(max_length=30) # nombre del ingrediente
    Precio = models.IntegerField(max_digits=10) # precio del ingrediente
    
class sub_receta(models.Model):
    nombre = models.CharField(max_length=30) # nombre de la subreceta
    descripcion = models.CharField(max_length=30) # descripcion de la subreceta
    ingredientes = models.ManyToManyField(Ingrediente) # ingredientes de la subreceta

class Receta(models.Model): 
    nombre = models.CharField(max_length=30) # nombre de la receta
    descripcion = models.CharField(max_length=300) # descripcion de la receta
    ingredientes = models.ManyToManyField(Ingrediente)# ingredientes de la receta
    sub_receta = models.ManyToManyField(sub_receta) # subreceta de la receta

    def __str__(self):
        return self.nombre
    
    def costo_total_receta(self):
        costo_total = 0 # inicializo la variable en 0
        for ingrediente in self.ingredientes.all(): # para cada ingrediente en los ingredientes
            costo_total += ingrediente.Precio # le agrego el precio a la variable costo total
        for subreceta in self.sub_receta.all(): # para cada subreceta en subreceta
            cantidad_utilizada = subreceta.receta_set.through.objects.get(sub_receta_id=subreceta.id, receta_id=self.id).cantidad_utilizada # Obtiene la cantidad utilizada de la subreceta en la receta actual
            costo_subreceta = subreceta.costo_total_subreceta() # Obtiene la cantidad utilizada de la subreceta actual
            costo_total += cantidad_utilizada * costo_subreceta # Obtiene la cantidad utilizada de la subreceta actual dependiendo de cuantas veces se utilizo 
        return costo_total # retorna la variable con el costo de la receta

            
    
# Usando el Many-to-Many en este caso, el campo ingredientes en el modelo Receta es un ManyToManyField que apunta al modelo Ingrediente.
# Esto permitirá que cada receta tenga varios ingredientes y cada ingrediente pueda estar presente en varias recetas

class Usuario(models.Model):
    nombre = models.CharField(max_length=30) # nombre de usuario
    password = models.CharField(max_length=30) # contraseña de usuario

    def __str__(self):
        return self.nombre + " " + self.password

