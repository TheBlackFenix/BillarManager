from django.db import models
from .tarifa import Tarifa
from .cliente import Cliente
from .mesa import Mesa

class Tiempo(models.Model):
    idTiempo = models.AutoField(primary_key=True)
    Ingreso = models.DateTimeField(auto_now=True)
    egreso = models.DateTimeField(null=True)
    idMesa = models.ForeignKey(Mesa, related_name='FKidMesa', on_delete=models.PROTECT)
    Observaciones = models.CharField(max_length=250)
    idCliente = models.ForeignKey(Cliente, related_name='FKDocumento', on_delete=models.PROTECT, null=True)
    idTarifa = models.ForeignKey(Tarifa, related_name='FKidTarifa', on_delete=models.PROTECT)