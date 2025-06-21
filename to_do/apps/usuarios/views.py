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
import threading
# Generar clave aleatoria
import string as st
import random as rd
from .models import Verificacion_correo
from django.http import HttpResponse


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
            contexto = {
                'first_name':request.data['first_name'].upper()
            }
            # Enviar correo de registro al usuario con threading para enviar correo de manera asincrona
            threading.Thread(target=envio_correo_registro, args=(self, request, 'Registro de usuario', request.data['email'], 'emails/registro.html', contexto)).start()
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
            print(request.build_absolute_uri())
            return Response({'update-basico':True},status=state.HTTP_200_OK)
        
        # Validar si solo va a cambiar la contraseña
        if request.data['clave']:
            usuario.set_password(request.data['basico']['password'])
            usuario.save()
            return Response({'update-password':True},status=state.HTTP_200_OK)

        # Validar si esta actualizando el correo
        if request.data['correo']:
            # Generar clave aleatoria
            clave_aleatoria = ''.join(rd.choices(st.ascii_letters + st.digits , k=75))
            verificacion = Verificacion_correo.objects.get_or_create(email=request.data['basico']['email'], token=clave_aleatoria, validez=True, usuario=usuario)

            # Datos para renderizar html de correo
            contexto = {
                'first_name':request.data['basico']['first_name'],
                'link':request.build_absolute_uri(f'/api/users/actualizar-perfil/correo?token={clave_aleatoria}&validate=1&email={request.data['basico']['email']}')
            }

            # Enviar correo de manera asincrona para email
            threading.Thread(target=envio_correo_registro, args=(self, request, 'Confirmación actualización de correo electronico', request.data['correo_antiguo'], 'emails/actualizar_email.html', contexto)).start()

            return Response({'update-correo':True},status=state.HTTP_200_OK)
        
        # Si hay algun problema en la actualizacion de datos enviar error de peticion
        return Response({'status':False},status=state.HTTP_400_BAD_REQUEST)

class LogoutUsuario(APIView):
    # El usuario ha cerrar sesion dede estar autenticado
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        response = Response({'logout':True},status=state.HTTP_200_OK)
        response.delete_cookie('access') # Eliminar la cookie con la autorizacion
        return response

# Vista para terminar de validar la actualizacion de correo electronico
class VerificacionLink(TemplateView):
    template_name = 'verification/verificacion_correo.html'

    def get(self, request):
        # Validar si el token es valido
        token = request.GET.get('token')
        validacion = request.GET.get('validate')
        correo = request.GET.get('email')

        credencial_validacion = Verificacion_correo.objects.get(token=token)
        if credencial_validacion.validar_token(correo, token, validacion) is not True:
            return super().get(request)
            
        return HttpResponse('Error en el token')


# Envio correo de confirmacion de registros y actualizacion de datos


def envio_correo_registro(self, request, asunto, correo, ruta_template, contexto):
    # Renderizar el html

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
    # Indicar que el contenido es html
    correo.attach_alternative(html, 'text/html')
    correo.send()
    return Response([],status=state.HTTP_200_OK)