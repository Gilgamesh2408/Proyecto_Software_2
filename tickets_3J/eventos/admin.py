from django.contrib import admin
from .models import Evento, Reserva, Boleta, Localidad, EventoLocalidad
from boletas.models import Compra


admin.site.register(Compra)
admin.site.register(Reserva)
admin.site.register(Evento)
admin.site.register(Localidad)
admin.site.register(EventoLocalidad)
