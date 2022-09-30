from dataclasses import fields
from pyexpat import model
from hospitalApp.models.usuarios import Usuario
from rest_framework import serializers

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['email','Contraseña','rol_usuario']