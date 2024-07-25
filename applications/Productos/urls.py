from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = 'producto_app'

urlpatterns = [
    path(
        'producto/detalles/<pk>/', #se detalla que registro segun su clave primaria desea detallar
        views.ProductoDetalles.as_view(),
        name='Detalles de producto',
    ),
    path(
        'producto/create/',
        views.ProductoCreateView.as_view(),
        name='Creacion de producto',
    ),  
    path(
        'producto/update/<pk>/', #se detalla que registro segun su clave primaria desea actualizar
        views.ProductoUpdateView.as_view(),
        name='Modificar producto'
    ),
    path(
        'producto/delete/<pk>/',
        views.ProductoDeleteView.as_view(),
        name='Borrar producto'
    ),
    path(
        'login/',
        views.LoginUser.as_view(),
        name='login-producto'
    ),
    path(
        'producto/panel/',
        views.Panel.as_view(),
        name='panel-producto'
    ),
    path(
        'producto/logout/',
        views.LogoutView.as_view(),
        name='logout-producto'
    ),
    path(
        'producto/ordenar/identificador',
        views.ProductoIdentificador.as_view(),
        name='producto-identificador'
    ),
    path(
        'producto/ordenar/nombre',
        views.ProductoNombre.as_view(),
        name='producto-nombre'
    ),
    path(
        'producto/ordenar/tipo',
        views.ProductoTipo.as_view(),
        name='producto-tipo'
    ),
    path(
        'producto/ordenar/marcaProd',
        views.ProductoMarca.as_view(),
        name='producto-marca'
    ),
    
    path(
        'producto/api',
        views.ProductoListApiView.as_view(),
        name='api-producto'
    ),
    
]