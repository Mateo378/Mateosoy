from django.shortcuts import render, redirect

from .models import Clientes
from .forms import formulario_clientes

# Create your views here.

def registrar_clientes(request):
    user_form=formulario_clientes(data=request.POST)
    if request.method=="POST":
        direccion=request.POST.get("direccion")
        telefono=request.POST.get("telefono")
        data_cliente=list()
        data_cliente.append([direccion, telefono])
        Clientes.objects.create(user=request.user,direccion=direccion,telefono=telefono)

        return redirect("Tienda")
    
    return render(request, "clientes/clientes.html", {"user_form":user_form})