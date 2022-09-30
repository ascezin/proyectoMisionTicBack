from django.db import models

class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    email = models.CharField('email', max_length = 100, unique=True)
    Contraseña = models.CharField('Contraseña', max_length = 100)
    rol_usuario = models.CharField('rol_usuario', max_length = 100)