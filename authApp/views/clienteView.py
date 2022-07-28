from rest_framework.views import APIView
from rest_framework.response import Response
from authApp.serializers.clienteSerializer import ClienteSerializer
from authApp.models.cliente import Cliente


class ClienteView(APIView):
    serializer_class = ClienteSerializer
    def get(self, request):
        cliente = Cliente.objects.all()
        cliente_serializer = ClienteSerializer(cliente, many = True)
        return Response(cliente_serializer.data)
    
    def post(self, request):
        cliente_serializar = ClienteSerializer(data = request.data)
        if cliente_serializar.is_valid():
            cliente_serializar.save()
            return Response("Guardado Correctamente")
        return Response(cliente_serializar.errors)
    
class ClienteDetail(APIView):
    def get(self,request, pk=None):
        cliente = Cliente.objects.filter(idCliente = pk).first()
        Cliente_serializer = ClienteSerializer(cliente)
        return Response(Cliente_serializer.data)

    def put(self,request, pk= None):
        cliente = Cliente.objects.filter(idCliente = pk).first()
        cliente_serializer = ClienteSerializer(cliente, data = request.data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return Response("Registro Actualizado")
        return Response(cliente_serializer.errors)
    
    def delete(self,request,pk):
        cliente = Cliente.objects.filter(idCliente = pk).first()
        msg = f'se elimino la cliente {cliente.idCliente}, Observaciones = {cliente.Observaciones}'
        cliente.delete()
        return Response(msg)
    
