from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
import rest_framework.status as state
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from .serializers import UsuarioSerializer
from django.views.generic import TemplateView

# Importar libreria json debido a que se envian datos en formato json
import json

# Create your views here.
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
            # Crear token de acceso
            access = RefreshToken.for_user(usuario)
            # Crear una cookie desde django y solo accecible en el servidor
            response = Response({'status':True,'access':str(access.access_token)},status=state.HTTP_200_OK)


            response.set_cookie(
                key='access',
                value=str(access.access_token),
                max_age=3600,
                httponly=True,
                secure=True,
                samesite='Strict'
            )
            # Retornar el json
            return response

        return Response({'status':False},status=state.HTTP_400_BAD_REQUEST)
        
# Registro de usuario
class Usuarios(APIView):
    # Permitir a cualquier usuario
    permission_classes = [AllowAny]

    def get(self, request):
        # Obtener todos los usuarios
        usuarios = User.objects.all()
        usuarios_json = UsuarioSerializer(usuarios, many=True).data
        # Devolver el json
        return Response(usuarios_json, status=state.HTTP_200_OK)

    def post(self, request):
        print("Entra")
        # Pasar los datos que llegan de la peticion al serializer
        user = UsuarioSerializer(data=request.data)

        if user.is_valid():
            # Crear el usuario
            user.save()
            return Response({'status':True},status=state.HTTP_200_OK)
        # Si no es valido
        return Response({'status':False},status=state.HTTP_400_BAD_REQUEST)

class LogoutUsuario(APIView):
    # El usuario ha cerrar sesion dede estar autenticado
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        response = Response({'logout':True},status=state.HTTP_200_OK)
        response.delete_cookie('access') # Eliminar la cookie con la autorizacion
        return response

