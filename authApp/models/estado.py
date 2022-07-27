from django.db import models

class Estado(models.Model):
    idEstado = models.AutoField(primary_key=True)
    Estado = models.CharField(max_length=30)