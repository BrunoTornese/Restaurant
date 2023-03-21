from django import forms
from models import *

class ingrediente_form(forms.ModelForm): # formulario de ingrediente
    class Meta:# clase meta para configurar el formulario
        model = Ingrediente # modelo del formulario
        fields = ['nombrer', 'precio'] # los valores que se van a poner en el formulario
    
class receta_form(forms.ModelForm): # formulario de receta
    class Meta:# clase meta para configurar el formulario
        model = Receta # modelo del formulario
        fields = ['nombrer', 'descripcion', 'ingredientes'] # los valores que se van a poner 

class sub_receta_form(forms.ModelForm): # formulario para la subreceta
    class Meta: # clase meta para configurar el formulario
        models = sub_receta # usa el models subreceta
        fields = ['nombre', 'descripcion', 'ingredientes'] # los valores que se van a poner

class editar_ingrediente_form(forms.ModelForm): # formulario de receta
    class Meta:# clase meta para configurar el formulario
        models = Ingrediente # modelo del formulario
        fields = ['nombrer', 'precio'] # los valores que se van a poner en el formilario

class editar_receta_form(forms.ModelForm): # formulario de receta
    class Meta:# clase meta para configurar el formulario
        models = Receta # modelo del formulario
        fields = ['nombrer', 'descripcion', 'ingredientes'] # los valores que se van a poner en el formulario

class ediar_sub_receta_form(forms.Model): # clase de editar subreceta
    class Meta: # clase meta para editar los valores
        models = sub_receta # modelo del formulario
        fields = ['nombre', 'descripcion', 'ingredientes'] # valores que se van a poner en el formulario

class Usuario_form(forms.ModelForm): # formulario de usuario
    class Meta:# clase meta para configurar el formulario
        models = Usuario # modelo del formulario
        fields = ['Usuario', 'Password'] # los valores que se van a poner en el formulario