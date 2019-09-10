from django.urls import path, include
from crud import views

urlpatterns = [
    path('', views.listar, name='listar'),
    path('guardar', views.guardar, name='guardar'),
    path('eliminar/<int:id>', views.eliminar, name="eliminar"),
    path('actualizar/<int:id>', views.actualizar_view, name="actualizar"),
]
