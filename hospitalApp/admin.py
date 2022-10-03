from django.contrib import admin
from .models.usuarios import Usuario
from .models.pacientes import Paciente

admin.site.register(Usuario)
admin.site.register(Paciente)