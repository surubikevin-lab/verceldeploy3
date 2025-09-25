from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # pantalla inicial con botones
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
]
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.user_login, name="login"),
    path("inicio/", views.inicio, name="inicio"),
    path("agregar/", views.agregar_producto, name="agregar_producto"),
    path("lista/", views.lista_productos, name="lista_productos"),
    path("logout/", views.user_logout, name="logout"),
]
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('inicio/', views.inicio, name='inicio'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('lista/', views.lista_productos, name='lista_productos'),
    
    # ¡FALTAN ESTAS URLs!
    path('editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
]