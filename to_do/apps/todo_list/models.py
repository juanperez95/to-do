from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Tareas(models.Model):

    # Datos para campo de estado de tarea
    class TareaEstado(models.TextChoices):
        TODO = 'TODO', _('Pendiente de realizar')
        EN_PROGRESO = 'EN_PROGRESO', _('En progreso')
        HECHO = 'HECHO', _('Realizado')

    class Meta:
        db_table = 'tareas'
        verbose_name = 'Tarea'
        # Orden de tabla
        ordering = ['-id']


    # Campos de la tabla tareas
    titulo = models.CharField('Titulo',max_length=100)
    descripcion = models.TextField('Descripción',blank=True,max_length=500)
    estado = models.CharField('Estado', choices=TareaEstado, default=TareaEstado.TODO)
    fecha_creacion = models.DateTimeField('Fecha de creación',auto_now_add=True, blank=True)
    fecha_modificacion = models.DateTimeField('Fecha de modificación',auto_now_add=True, blank=True)
    # Llave foranea de usuarios para saber que tareas tiene
    user = models.ForeignKey(User, on_delete=models.CASCADE)