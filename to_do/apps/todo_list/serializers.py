from rest_framework import serializers
from .models import Tareas
from django.contrib.auth.models import User

class TareasSerializer(serializers.ModelSerializer):

    # Validaciones del serializador 
    titulo = serializers.CharField(max_length=100)
    descripcion = serializers.CharField(max_length=500)
    estado = serializers.CharField(max_length=100)
    fecha_creacion = serializers.DateTimeField()
    fecha_modificacion = serializers.DateTimeField()

    class Meta:
        model = Tareas
        fields = ['titulo','descripcion','estado','fecha_creacion','fecha_modificacion']

