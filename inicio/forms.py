from django import forms

class FormularioCrearAuto(forms.Form):
    marca= forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder':'fiat, ford'}))
    modelo= forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder':'Cronos, Aveo'}))
    
class FormularioBusqueda(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
    modelo = forms.CharField(max_length=20, required=False)
    