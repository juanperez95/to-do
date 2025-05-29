from django.shortcuts import render
from .models import Tareas
# Importar los serializers
from .serializers import TareasSerializer

# Atenticar el usuario si esta en la base de datos
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
# Para proteger las funciones de la api si no esta logueado el usuario
from rest_framework.permissions import IsAuthenticated
import rest_framework.status as state
from django.contrib.auth.models import User


# Importar libreria json debido a que se envian datos en formato json
import json

# Create your views here.
class ApiTodo(APIView):

    # Permitir solo usuarios logueados
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Obtener todas las tareas
        todos = Tareas.objects.filter(user=request.user.id)
        todos_json = TareasSerializer(todos, many=True).data
        # Devolver el json
        return Response(todos_json, status=state.HTTP_200_OK)

    # Crear tarea
    def post(self, request):
        # Pasar los datos que llegan de la peticion al serializer
        data = request.data
        data['user'] = request.user.id
        tarea = TareasSerializer(data=data)
        # Validar el serializador
        if tarea.is_valid():
            # Crear el tarea
            tarea.save()
            return Response({'created':True},status=state.HTTP_200_OK)
        print(tarea.errors)
        

        # Si no es valido
        return Response({'created':False},status=state.HTTP_400_BAD_REQUEST)
    
    # Eliminar la tarea de la base de datos
    def delete(self, request, pk):
        try:
            tarea = Tareas.objects.get(pk=pk)
            tarea.delete()
        except Tareas.DoesNotExist:
            return Response({'deleted':False},status=state.HTTP_404_NOT_FOUND)
        return Response({'deleted':True},status=state.HTTP_200_OK)
    

# Actualizar si la tarea esta hecha
class TodoUpdate(APIView):

    # Permitir solo usuarios logueados
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            tarea = Tareas.objects.get(pk=pk) # Buscar la tarea con el id
            tarea.estado = "HECHO"
            tarea.save() # Guardar el estado de hecho
            return Response({'updated':True},status=state.HTTP_200_OK)
        except Tareas.DoesNotExist:
            pass
        # Si no devuelve que no se pudo actualizar
        return Response({'updated':False},status=state.HTTP_404_NOT_FOUND)
        

