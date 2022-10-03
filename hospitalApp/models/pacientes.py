from django.db import models
from .usuarios import Usuario

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    Nombre = models.CharField('Nombre', max_length = 100)
    Apellido = models.CharField('Apellido', max_length = 100)
    Cedula = models.CharField('Cedula', max_length = 100)
    Celular = models.CharField('Celular', max_length = 100)
    Direccion = models.CharField('Direccion', max_length = 100)
    usuario_id = models.ForeignKey(Usuario, related_name='usuario_paciente_id', on_delete=models.CASCADE)
