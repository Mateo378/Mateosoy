from django import forms

class formulario_clientes(forms.Form):
    direccion=forms.CharField(max_length=50)
    telefono=forms.IntegerField()