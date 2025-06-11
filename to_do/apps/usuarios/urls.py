from django.urls import path
from .views import LoginUsuario, Usuarios, LogoutUsuario

# Nombre de rutas de la aplicacion
app_name = 'usuarios'
urlpatterns = [
    # Rutas para el usuario
    path('login', LoginUsuario.as_view(), name='login'), # Login de usuario
    path('', Usuarios.as_view(), name='usuarios'),
    path('logout', LogoutUsuario.as_view(), name='logout'), # Cerrar la sesion
    path('actualizar-perfil', Usuarios.as_view(), name='actualizar-perfil'), # Actualizar el perfil
]