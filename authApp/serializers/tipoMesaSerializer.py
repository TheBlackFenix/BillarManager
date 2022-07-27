from rest_framework import serializers
from authApp.models.tipoMesa import TipoMesa

class TipoMesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMesa
        fields = '__all__'
