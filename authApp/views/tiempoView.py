from rest_framework.views import APIView
from rest_framework.response import Response
from authApp.serializers.tiempoSerializer import TiempoSerializer
from authApp.models.tiempo import Tiempo


class TiempoView(APIView):
    serializer_class = TiempoSerializer
    
    def get(self, request):
        tiempo = Tiempo.objects.all()
        tiempo_serializer = TiempoSerializer(tiempo, many = True)
        return Response(tiempo_serializer.data)
    
    def post(self, request):
        tiempo_serializer = TiempoSerializer(data = request.data)
        if tiempo_serializer.is_valid():
            tiempo_serializer.save()
            return Response("Guardado Correctamente")
        return Response(tiempo_serializer.errors)
    
class TiempoDetail(APIView):
    def get(self,request, pk=None):
        tiempo = Tiempo.objects.filter(idTipo = pk).first()
        Tiempo_serializer = TiempoSerializer(tiempo)
        return Response(Tiempo_serializer.data)

    def put(self,request, pk= None):
        tiempo = Tiempo.objects.filter(idTipo = pk).first()
        mesa_serializer = TiempoSerializer(tiempo, data = request.data)
        if mesa_serializer.is_valid():
            mesa_serializer.save()
            return Response("Registro Actualizado")
        return Response(mesa_serializer.errors)
    
    def delete(self,request,pk):
        tiempo = Tiempo.objects.filter(idTipo = pk).first()
        msg = f'se elimino la tiempo {tiempo.idTiempo}, Observaciones = {tiempo.Observaciones}'
        tiempo.delete()
        return Response(msg)