# Generated by Django 4.0.6 on 2022-07-29 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0002_alter_tiempo_egreso_alter_tiempo_idcliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiempo',
            name='Ingreso',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
