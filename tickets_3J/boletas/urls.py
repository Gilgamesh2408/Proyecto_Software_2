from django.urls import path
from . import views

urlpatterns = [
    path('comprar_boletas/<int:evento_id>/', views.comprar_boletas, name='comprar_boletas'),
    path('confirmar_compra/<int:evento_id>/', views.confirmar_compra, name='confirmar_compra'),
]
