from dataclasses import fields
from pyexpat import model
from hospitalApp.models.usuarios import Usuario
from hospitalApp.models.pacientes import Paciente
from rest_framework import serializers

class pacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['Nombre','Apellido','Cedula','Celular','Direccion','usuario_id']