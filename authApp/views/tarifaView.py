from rest_framework.views import APIView
from rest_framework.response import Response
from authApp.serializers.tarifaSerializer import TarifaSerializer
from authApp.models.tarifa import Tarifa


class TarifaView(APIView):
    serializer_class = TarifaSerializer
    def get(self, request):
        tarifa = Tarifa.objects.all()
        tarifa_serializer = TarifaSerializer(tarifa, many = True)
        return Response(tarifa_serializer.data)
    
    def post(self, request):
        tarifa_serializer = TarifaSerializer(data = request.data)
        if tarifa_serializer.is_valid():
            tarifa_serializer.save()
            return Response("Guardado Correctamente")
        return Response(tarifa_serializer.errors)
    
class TarifaDetail(APIView):
    def get(self,request, pk=None):
        tarifa = Tarifa.objects.filter(idTipo = pk).first()
        Tarifa_serializer = TarifaSerializer(tarifa)
        return Response(Tarifa_serializer.data)

    def put(self,request, pk= None):
        tarifa = Tarifa.objects.filter(idTipo = pk).first()
        mesa_serializer = TarifaSerializer(tarifa, data = request.data)
        if mesa_serializer.is_valid():
            mesa_serializer.save()
            return Response("Registro Actualizado")
        return Response(mesa_serializer.errors)
    
    def delete(self,request,pk):
        tarifa = Tarifa.objects.filter(idTipo = pk).first()
        msg = f'se elimino la tarifa {tarifa.idTarifa}, Observaciones = {tarifa.Observaciones}'
        tarifa.delete()
        return Response(msg)