from django.db import models
from .estado import Estado
from .tipoMesa import TipoMesa

class Mesa(models.Model):
    idMesa = models.AutoField(primary_key=True)
    idTipo = models.ForeignKey(TipoMesa, related_name= 'FKidTipo', on_delete=models.PROTECT)
    idEstado = models.ForeignKey(Estado, related_name= 'FKidEstado', on_delete=models.PROTECT)
    Observaciones = models.CharField(max_length=250)