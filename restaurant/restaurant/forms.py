from django import forms
from models import *

class ingrediente_form(forms.ModelForm): # formulario de ingrediente
    class Meta:# clase meta para configurar el formulario
        model = Ingrediente # modelo del formulario
        fields = ['nombrer', 'precio'] # los valores que se van a poner en el formulario
    
class receta_form(forms.ModelForm): # formulario de receta
    class Meta:# clase meta para configurar el formulario
        model = Receta # modelo del formulario
        fields = ['nombrer', 'descripcion', 'ingredientes'] # los valores que se van a poner en el


class editar_ingrediente_form(forms.ModelForm): # formulario de receta
    class Meta:# clase meta para configurar el formulario
        models = Ingrediente # modelo del formulario
        fields = ['nombrer', 'precio'] # los valores que se van a poner en el formilario

class editar_receta_form(forms.ModelForm): # formulario de receta
    class Meta:# clase meta para configurar el formulario
        models = Receta # modelo del formulario
        fields = ['nombrer', 'descripcion', 'ingredientes'] # los valores que se van a