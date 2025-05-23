from rest_framework import serializers
from django.contrib.auth.models import User

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
        fields = ['username','first_name','last_name','email']

    def create(self, validated_data):
        # Crear el usuario
        usuario = User.objects.create_user(**validated_data)
        return usuario