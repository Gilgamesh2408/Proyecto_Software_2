from django.urls import path

from . import views
from commons.views import perfil_usuario

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.index, name='index'),
    path('registro',views.registro,name='registro'),
    path('perfil/', perfil_usuario, name='perfil_usuario')
]