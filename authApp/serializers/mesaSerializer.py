from rest_framework import serializers
from authApp.models.mesa import Mesa

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'
