
from django.contrib import admin
from django.urls import path, include

# Rutas de la aplicacion todo-list
app_name = 'to_do'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.todo_list.urls')),
]
