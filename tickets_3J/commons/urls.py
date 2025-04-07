from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.index, name='index'),
    path('registro',views.registro,name='registro')
]