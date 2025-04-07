# eventos/models.py

from django.db import models
from django.contrib.auth.models import User

# Modelos de la aplicación eventos

class Localidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50)
    total_boletas = models.PositiveIntegerField()  # Total de boletas para el evento
    imagen = models.FileField(upload_to="eventos/", null=True, blank=True)

    def __str__(self):
        return self.nombre

class EventoLocalidad(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    boletas_disponibles = models.PositiveIntegerField()

    class Meta:
        unique_together = ('evento', 'localidad')  # Asegura que no haya duplicados de eventos y localidades

    def __str__(self):
        return f"{self.evento.nombre} - {self.localidad.nombre}"


# Modelos de la aplicación boletas

class Boleta(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Boleta {self.id} - {self.evento.nombre} - {self.localidad.nombre}"


# Modelo de la aplicación reservas

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    boleta = models.OneToOneField(Boleta, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva {self.id} por {self.usuario.username} para {self.boleta.evento.nombre}"
