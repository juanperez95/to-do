from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Verificacion_correo(models.Model):

    class Meta:
        verbose_name = 'Verificacion correo'
        db_table = 'verificacion_correo'

    email = models.EmailField(max_length=255, unique=True, blank=True, null=True) # email nuevo
    token = models.CharField(max_length=255, blank=True, null=True) # Token generado en el sistema
    validez = models.BooleanField(default=False) # Si el token tiene validez
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # Relacion con el usuario

    def __str__(self):
        return self.email

    # Funcion para cada modelo de validar si el token corresponde al email y si es valido
    def validar_token(self, email, token, id_usuario):
        if self.email == email and self.token == token and self.validez and self.usuario.id == id_usuario:
            return True
        return False