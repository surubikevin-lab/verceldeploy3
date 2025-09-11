from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # pantalla inicial con botones
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
]
