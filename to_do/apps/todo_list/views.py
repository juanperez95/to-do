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


# Importar libreria json debido a que se envian datos en formato json
import json

# Create your views here.
class ApiTodo(APIView):

    # Permitir solo usuarios logueados
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Obtener todas las tareas
        todos = Tareas.objects.all()
        todos_json = TareasSerializer(todos, many=True).data
        # Devolver el json
        return Response(todos_json, status=state.HTTP_200_OK)


        

