from django.shortcuts import render
from .models import Tareas
# Importar los serializers
from .serializers import TareasSerializer
from django.contrib.auth.models import User
# Atenticar el usuario si esta en la base de datos
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
# Para proteger las funciones de la api si no esta logueado el usuario
from rest_framework.permissions import IsAuthenticated,AllowAny
import rest_framework.status as state
from rest_framework_simplejwt.tokens import RefreshToken

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
        return Response(todos_json)

# Login de usuario
class LoginUsuario(APIView):

    permission_classes = [AllowAny] # Cualquiera ingresa

    def post(self,request):
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        # Autenticar el usuario
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario) # Iniciar sesion
            return Response({'status':True},status=state.HTTP_200_OK)
        else:
            return Response({'status':False},status=state.HTTP_400_BAD_REQUEST)

