from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()

class Clientes(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    direccion=models.CharField(max_length=50)
    telefono=models.IntegerField()

    def __str__(self):
        return f'El usuario {self.user} con direccion {self.direccion} y numero de telefono {self.telefono}'

    
    class Meta:
        db_table="Clientes"
        verbose_name="Cliente"
        verbose_name_plural="Clientes"
        ordering=['id']
