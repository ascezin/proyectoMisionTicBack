from itertools import product
from urllib.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from hospitalApp.models import Paciente
from hospitalApp.serializers import pacienteSerializer
from hospitalApp.models import Usuario
from hospitalApp.serializers import userSerializer

@api_view(['GET','POST'])
def pacientes_api_view(request):

    if request.method == 'GET':
        paciente = Paciente.objects.all()
        paciente_serializer = pacienteSerializer(paciente, many=True)
        return Response(paciente_serializer.data)

    elif request.method == 'POST':
        paciente_serializer = pacienteSerializer(data = request.data)
        if paciente_serializer.is_valid():
            paciente_serializer.save()
            return Response("Se ha registrado correctamente")
        return Response(paciente_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def pacientes_detail_view(request,pk=None):
    if request.method == 'GET':
        usuario = Paciente.objects.filter(id_paciente = pk).first()
        paciente_serializer = pacienteSerializer(usuario)
        return Response(paciente_serializer.data)
    if request.method == 'PUT':
        paciente = Paciente.objects.filter(id_paciente = pk).first()
        paciente_serializer = pacienteSerializer(instance=paciente, data=request.data)
        if paciente_serializer.is_valid():
            paciente_serializer.save()
            return Response("Paciente Actualizado")
        return Response (paciente_serializer.errors)
    if request.method == 'DELETE':
        paciente = Paciente.objects.filter(id_paciente = pk).first()
        paciente.delete()
        return Response("Paciente Eliminado...")