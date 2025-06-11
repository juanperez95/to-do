from django.urls import path
from .views import ApiTodo, TodoUpdate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'todo' # Distinguir entre las rutas de la aplicacion
urlpatterns = [
    path('', ApiTodo.as_view(), name='index'),
    # Validar rutas para saber si funcionan los tokens (SOLO PRUEBA)
    path('token',TokenObtainPairView.as_view(), name='token'),
    path('refresh',TokenRefreshView.as_view(), name='refresh'),
    # Rutas para tareas
    path('<uuid:pk>', ApiTodo.as_view(), name='tareas'), # Eliminar o actuallizar la tarea
    path('actualizar/<uuid:pk>',TodoUpdate.as_view(), name='actualizar_tarea') # Actualziar la tarea
]