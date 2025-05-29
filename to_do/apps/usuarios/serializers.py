from rest_framework import serializers
from django.contrib.auth.models import User
from apps.todo_list.models import Tareas

# Usuarios
class UsuarioSerializer(serializers.ModelSerializer):

    # Validaciones del serializador 
    username = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()    

    class Meta:
        model = User
        # Solo mostrar estos campos
        fields = ['username','first_name','last_name','email','password']

    def create(self, validated_data):
        # Crear el usuario
        usuario = User.objects.create_user(**validated_data)
        # Registrar una tarea por defecto cuando se registra un usuario
        tarea = Tareas(titulo='Tarea inicial',descripcion='Descripcion de la tarea',estado='TODO',user=usuario)
        tarea.save()
        return usuario