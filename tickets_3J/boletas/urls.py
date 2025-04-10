from django.urls import path
from . import views
from .views import obtener_ventas

urlpatterns = [
    path('comprar_boletas/<int:evento_id>/', views.comprar_boletas, name='comprar_boletas'),
    path('confirmar_compra/<int:evento_id>/', views.confirmar_compra, name='confirmar_compra'),
    path('reportes/eventos/', views.reporte_eventos, name='reporte_eventos'),
    path('api/ventas/', views.obtener_ventas, name='api-ventas'),
]
# boletas/api/ventas/