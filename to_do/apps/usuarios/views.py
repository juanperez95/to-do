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
# Envio de correos y renderizacion  de HTML
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string

# Importar libreria json debido a que se envian datos en formato json
import json

# Create your views here.
# Login de usuario
class LoginUsuario(APIView):

    permission_classes = [AllowAny] # Cualquiera ingresa

    def get(self,request):
        return Response({'user':f"{request.user.first_name} {request.user.last_name}".title()},status=state.HTTP_200_OK)

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
        # obtener el usuario que ha iniciado sesion
        try:
            usuario = User.objects.get(id=request.user.id)
            usuarioSerializer = UsuarioSerializer(usuario).data # Serializar el usuario

            return Response({'usuario':usuarioSerializer}, status=state.HTTP_200_OK) # Devolver OK
        except User.DoesNotExist as e:
            pass
        # Devolver el json en caso de algun problema con la peticion
        return Response({'usuario':False}, status=state.HTTP_404_NOT_FOUND)

    def post(self, request):
        print("Entra")
        # Pasar los datos que llegan de la peticion al serializer
        user = UsuarioSerializer(data=request.data)

        if user.is_valid():
            # Crear el usuario
            user.save()
            # Enviar correo de registro al usuario
            envio_correo_registro(self, request, 'Registro de usuario', request.data['email'], 'emails/registro.html')
            return Response({'status':True},status=state.HTTP_200_OK)
        # Si no es valido
        return Response({'status':False},status=state.HTTP_400_BAD_REQUEST)


    def patch(self, request):
        # Validar si solo se va actualizar la info basica del perfil
        usuario = User.objects.get(id=request.user.id) # Obtener el usuario
        if request.data['info_basica']:
            usuario.first_name = request.data['basico']['first_name']
            usuario.last_name = request.data['basico']['last_name']
            usuario.username = request.data['basico']['username']
            usuario.save()
            return Response({'update-basico':True},status=state.HTTP_200_OK)
        
        # Validar si solo va a cambiar la contraseña
        if request.data['clave']:
            usuario.set_password(request.data['password'])
            usuario.save()
            return Response({'update-password':True},status=state.HTTP_200_OK)

class LogoutUsuario(APIView):
    # El usuario ha cerrar sesion dede estar autenticado
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        response = Response({'logout':True},status=state.HTTP_200_OK)
        response.delete_cookie('access') # Eliminar la cookie con la autorizacion
        return response


# Envio correo de confirmacion de registros y actualizacion de datos


def envio_correo_registro(self, request, asunto, correo, ruta_template):
    # Renderizar el html
    contexto = {
        'first_name':request.data['first_name'].upper()
    }

    html = render_to_string(ruta_template, contexto)
    # Renderizar el texto
    texto = strip_tags(html)
    # Enviar el correo
    correo = EmailMultiAlternatives(
        subject=asunto,
        body=texto,
        from_email='juanperez@gmail.com',
        to=[correo]
    )
    correo.attach_alternative(html, 'text/html')
    correo.send()
    return Response([],status=state.HTTP_200_OK)