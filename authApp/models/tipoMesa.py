from django.db import models

class TipoMesa(models.Model):
    idTipo = models.AutoField(primary_key=True)
    TipoMesa = models.CharField(max_length=30)