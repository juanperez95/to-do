from django.urls import path
from .views import LoginUsuario, Usuarios

# Nombre de rutas de la aplicacion
app_name = 'usuarios'
urlpatterns = [
    # Rutas para el usuario
    path('login', LoginUsuario.as_view(), name='login'),
    path('', Usuarios.as_view(), name='usuarios'),
]