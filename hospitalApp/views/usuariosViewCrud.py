from itertools import product
from urllib.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from hospitalApp.models import Usuario
from hospitalApp.serializers import userSerializer

@api_view(['GET','POST'])
def usuarios_api_view(request):

    if request.method == 'GET':
        usuario = Usuario.objects.all()
        usuario_serializer = userSerializer(usuario, many=True)
        return Response(usuario_serializer.data)

    elif request.method == 'POST':
        usuario_serializer = userSerializer(data = request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response("Se ha registrado correctamente")
        return Response(usuario_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def usuarios_detail_view(request,pk=None):
    if request.method == 'GET':
        usuario = Usuario.objects.filter(usuario_id = pk).first()
        usuario_serializer = userSerializer(usuario)
        return Response(usuario_serializer.data)
    if request.method == 'PUT':
        usuario = Usuario.objects.filter(usuario_id = pk).first()
        usuario_serializer = userSerializer(instance=usuario, data=request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response("usuario Actualizado")
        return Response (usuario_serializer.errors)
    if request.method == 'DELETE':
        usuario = Usuario.objects.filter(usuario_id = pk).first()
        usuario.delete()
        return Response("Usuario Eliminado...")