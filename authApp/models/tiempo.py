from django.db import models
from .tarifa import Tarifa
from .cliente import Cliente
from .mesa import Mesa

class Tiempo(models.Model):
    idTiempo = models.AutoField(primary_key=True)
    Ingreso = models.DateTimeField()
    egreso = models.DateTimeField()
    idMesa = models.ForeignKey(Mesa, related_name='FKidMesa', on_delete=models.DO_NOTHING)
    Observaciones = models.CharField(max_length=250)
    idCliente = models.ForeignKey(Cliente, related_name='FKDocumento', on_delete=models.DO_NOTHING)
    idTarifa = models.ForeignKey(Tarifa, related_name='FKidTarifa', on_delete=models.DO_NOTHING)