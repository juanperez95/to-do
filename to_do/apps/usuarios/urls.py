from django.urls import path
from .views import LoginUsuario, Usuarios, LogoutUsuario, AuthUsuario

# Nombre de rutas de la aplicacion
app_name = 'usuarios'
urlpatterns = [
    # Rutas para el usuario
    path('login', LoginUsuario.as_view(), name='login'), # Login de usuario
    path('', Usuarios.as_view(), name='usuarios'),
    path('logout', LogoutUsuario.as_view(), name='logout'), # Cerrar la sesion
    path('auth', AuthUsuario.as_view(), name='auth-usuario'), # Validar la sesion
]