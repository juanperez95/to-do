
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


# Rutas de la aplicacion todo-list
app_name = 'to_do'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todos/', include('apps.todo_list.urls')), # Rutas de las tareas
    path('api/users/', include('apps.usuarios.urls')), # Rutas de los usuarios

]
