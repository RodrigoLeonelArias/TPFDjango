from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = 'cliente_app' 

urlpatterns = [
    path(
        'cliente/detalles/<pk>/', #En pk ira el numero de la clave primaria
        views.ClienteDetalles.as_view(),
        name='Detalles de Clientes',
    ),
    path(
        'cliente/create/',
        views.ClienteCreateView.as_view(),
        name='Creacion de Cliente',
    ),
    path(
        'cliente/update/<pk>/', #se detalla que registro segun su clave primaria desea actualizar
        views.ClienteUpdateView.as_view(),
        name='Modificar Cliente'
    ),
    path(
        'cliente/delete/<pk>/',
        views.ClienteDeleteView.as_view(),
        name='Borrar Cliente'
    ),
    path(
        'login/',
        views.LoginUser.as_view(),
        name='login-cliente'
    ),
    path(
        'cliente/panel/',
        views.Panel.as_view(),
        name='panel-cliente'
    ),
    path(
        'cliente/logout/',
        views.LogoutView.as_view(),
        name='logout-cliente'
    ),
    path(
        'cliente/ordenar/dni',
        views.ClienteDni.as_view(),
        name='cliente-dni'
    ),
    path(
        'cliente/ordenar/nombre',
        views.ClienteNombre.as_view(),
        name='cliente-nombre'
    ),
    path(
        'cliente/ordenar/apellido',
        views.ClienteApellido.as_view(),
        name='cliente-apellido'
    ),
    
    path(
        'cliente/api',
        views.ClienteListApiView.as_view(),
        name='api-cliente'
    ),
]