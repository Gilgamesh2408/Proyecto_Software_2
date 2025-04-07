from django.db import models
from django.contrib.auth.models import User
from eventos.models import Evento

class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario que compra
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)  # Evento para el cual se compra
    cantidad = models.PositiveIntegerField()  # Cantidad de boletas compradas
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha en la que se realiza la compra

    def __str__(self):
        return f'Compra hecha por {self.usuario} para el evento {self.evento.nombre}  y compro {self.cantidad} boletas '
