from django.contrib import admin
from django.urls import path, re_path, include
from . import views 

app_name = 'preventista_app' 

urlpatterns = [
    path(
        'preventistas/detalles/<pk>/',
        views.ProveedorDetalles.as_view(),
        name='Detalles de proveedor'
    ),
    path(
        'preventistas/create/',
        views.ProveedorCreateView.as_view(),
        name='Creacion de proveedor'
    ),
    path(
        'preventistas/update/<pk>/',
        views.ProveedorUpdateView.as_view(),
        name='Modificar proveedor'
    ),
    path(
        'preventistas/delete/<pk>/',
        views.ProveedorDeleteView.as_view(),
        name='Borrar proveedor'
    ),
    path(
        'login/',
        views.LoginUser.as_view(),
        name='login-proveedor'
    ),
    path(
        'preventistas/panel/',
        views.Panel.as_view(),
        name='panel-proveedor'
    ),
    path(
        'preventistas/logout/',
        views.LogoutView.as_view(),
        name='logout-proveedor'
    ),
    path(
        'preventistas/ordenar/identificador',
        views.ProveedorIdentificador.as_view(),
        name='proveedor-identificador'
    ),
    path(
        'preventistas/ordenar/nombre',
        views.ProveedorNombre.as_view(),
        name='proveedor-nombre'
    ),
    path(
        'preventistas/ordenar/rubro',
        views.ProveedorRubro.as_view(),
        name='proveedor-rubro'
    ),
    path(
        'preventistas/api',
        views.ProveedorListApiView.as_view(),
        name='api-proveedor'
    ),
]