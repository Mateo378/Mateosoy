from django.urls import path
from .views import VRegistro, cerrar_sesion, log_in

urlpatterns = [
    path('', VRegistro.as_view(), name="login"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('entrar', log_in, name="entrar"),
]