from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_login, name="login"),
    path("inicio/", views.inicio, name="inicio"),
    path("agregar/", views.agregar_producto, name="agregar_producto"),
    path("lista/", views.lista_productos, name="lista_productos"),
    path("editar/<int:pk>/", views.editar_producto, name="editar_producto"),
    path("eliminar/<int:pk>/", views.eliminar_producto, name="eliminar_producto"),
    path("logout/", views.user_logout, name="logout"),
]
