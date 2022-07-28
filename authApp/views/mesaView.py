from rest_framework.views import APIView
from rest_framework.response import Response
from authApp.serializers.mesaSerializer import MesaSerializer
from authApp.models.mesa import Mesa


class MesaView(APIView):
    serializer_class = MesaSerializer
    def get(self, request):
        mesa = Mesa.objects.all()
        mesa_serializer = MesaSerializer(mesa, many = True)
        return Response(mesa_serializer.data)
    
    def post(self, request):
        mesa_serializar = MesaSerializer(data = request.data)
        if mesa_serializar.is_valid():
            mesa_serializar.save()
            return Response("Guardado Correctamente")
        return Response(mesa_serializar.errors)
    
class MesaDetail(APIView):
    def get(self,request, pk=None):
        mesa = Mesa.objects.filter(idMesa = pk).first()
        Mesa_serializer = MesaSerializer(mesa)
        return Response(Mesa_serializer.data)

    def put(self,request, pk= None):
        mesa = Mesa.objects.filter(idMesa = pk).first()
        mesa_serializer = MesaSerializer(mesa, data = request.data)
        if mesa_serializer.is_valid():
            mesa_serializer.save()
            return Response("Registro Actualizado")
        return Response(mesa_serializer.errors)
    
    def delete(self,request,pk):
        mesa = Mesa.objects.filter(idMesa = pk).first()
        msg = f'se elimino la mesa {mesa.idMesa}, Observaciones = {mesa.Observaciones}'
        mesa.delete()
        return Response(msg)
    
