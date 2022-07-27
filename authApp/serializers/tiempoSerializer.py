from rest_framework import serializers
from authApp.models.tiempo import Tiempo

class TiempoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiempo
        fields = '__all__'
