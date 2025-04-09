from rest_framework import serializers
from .models import Compra 


class VentaSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()  
    evento = serializers.CharField(source='evento.nombre')  

    class Meta:
        model = Compra
        fields = ['usuario', 'evento', 'cantidad', 'fecha']  