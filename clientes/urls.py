from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar_clientes, name="clientes"),
]