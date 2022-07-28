from rest_framework.views import APIView
from rest_framework.response import Response
from authApp.serializers.tipoMesaSerializer import TipoMesaSerializer
from authApp.models.tipoMesa import TipoMesa


class TipoMesaView(APIView):
    serializer_class = TipoMesaSerializer
    def get(self, request):
        tipoMesa = TipoMesa.objects.all()
        tipoMesa_serializer = TipoMesaSerializer(tipoMesa, many = True)
        return Response(tipoMesa_serializer.data)
    
    def post(self, request):
        tipoMesa_serializer = TipoMesaSerializer(data = request.data)
        if tipoMesa_serializer.is_valid():
            tipoMesa_serializer.save()
            return Response("Guardado Correctamente")
        return Response(tipoMesa_serializer.errors)
    
class TipoMesaDetail(APIView):
    def get(self,request, pk=None):
        tipoMesa = TipoMesa.objects.filter(idTipo = pk).first()
        TipoMesa_serializer = TipoMesaSerializer(tipoMesa)
        return Response(TipoMesa_serializer.data)

    def put(self,request, pk= None):
        tipoMesa = TipoMesa.objects.filter(idTipo = pk).first()
        mesa_serializer = TipoMesaSerializer(tipoMesa, data = request.data)
        if mesa_serializer.is_valid():
            mesa_serializer.save()
            return Response("Registro Actualizado")
        return Response(mesa_serializer.errors)
    
    def delete(self,request,pk):
        tipoMesa = TipoMesa.objects.filter(idTipo = pk).first()
        msg = f'se elimino la tipoMesa {tipoMesa.idTipoMesa}, Observaciones = {tipoMesa.Observaciones}'
        tipoMesa.delete()
        return Response(msg)