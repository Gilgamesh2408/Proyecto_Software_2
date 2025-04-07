from django.urls import path
from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('',views.productosIndex, name='EventosIndex'),
    path('detalle/<id>/',views.detalleProducto, name='detalleEvento'),
    #path('editar/<id>/',views.editarProducto, name='editarProductos'),
    path('borrar/<id>/',views.eliminarBoleta, name='eliminarBoleta'),
]