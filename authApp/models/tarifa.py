from django.db import models

class Tarifa(models.Model):
    idTarifa = models.AutoField(primary_key=True)
    Tarifa = models.CharField(max_length=50)
    ValorMinuto = models.IntegerField()
    Estado = models.BooleanField(default=1)
    