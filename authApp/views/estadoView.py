from rest_framework.views import APIView
from rest_framework.response import Response
from authApp.models import estado
from authApp.serializers.estadoSerializer import EstadoSerializer
from authApp.models.estado import Estado


class EstadoView(APIView):
    serializer_class = Estado
    def get(self, request):
        estado = Estado.objects.all()
        estado_serializer = EstadoSerializer(estado, many = True)
        return Response(estado_serializer.data)
    
    def post(self, request):
        estado_serializer = EstadoSerializer(data = request.data)
        if estado_serializer.is_valid():
            estado_serializer.save()
            return Response("Guardado Correctamente")
        return Response(estado_serializer.errors)

class EstadoDetail(APIView):
    def get(self,request, pk=None):
        estado = Estado.objects.filter(idEstado = pk).first()
        estado_serializer = EstadoSerializer(estado)
        return Response(estado_serializer.data)

    def put(self,request, pk= None):
        estado = Estado.objects.filter(idEstado = pk).first()
        estado_serializer = EstadoSerializer(estado, data = request.data)
        if estado_serializer.is_valid():
            estado_serializer.save()
            return Response("Registro Actualizado")
        return Response(estado_serializer.errors)
    
    def delete(self,request,pk):
        estado = Estado.objects.filter(idEstado = pk).first()
        msg = f'se elimino la estado {estado.idEstado}, Observaciones = {estado.Observaciones}'
        estado.delete()
        return Response(msg)