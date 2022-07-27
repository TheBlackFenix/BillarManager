from django.db import models

class Cliente(models.Model):
    Documento = models.CharField(primary_key= True, max_length= 20)
    Nombre = models.CharField(max_length=50)
    NickName = models.CharField(max_length=20)
    FechaRegistro = models.DateField()
    FechaNacimiento = models.DateField()