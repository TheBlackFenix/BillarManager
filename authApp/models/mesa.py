from distutils.archive_util import make_zipfile
from email.errors import InvalidMultipartContentTransferEncodingDefect
import imp
from pyexpat import model
from django.db import models
from .estado import Estado
from .tipoMesa import TipoMesa

class Mesa(models.Model):
    idMesa = models.AutoField(primary_key=True)
    idTipo = models.ForeignKey(TipoMesa, related_name= 'FKidTipo', on_delete=models.DO_NOTHING)
    idEstado = models.ForeignKey(Estado, related_name= 'FKidEstado', on_delete=models.DO_NOTHING)
    Observaciones = models.CharField(max_length=250)