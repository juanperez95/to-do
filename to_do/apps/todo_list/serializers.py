from rest_framework import serializers
from .models import Tareas
from .models import Tareas

class TareasSerializer(serializers.ModelSerializer):

    # Validaciones del serializador 
    titulo = serializers.CharField(max_length=100)
    descripcion = serializers.CharField(max_length=500)
    estado = serializers.CharField(max_length=100)

    class Meta:
        model = Tareas
        fields = ['id','titulo','descripcion','estado','fecha_creacion','fecha_modificacion','user']


