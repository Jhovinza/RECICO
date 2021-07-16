from django.urls import path
from Aplicacion.views import Aplicacion, inicio, listaClientes, agregarClientes, modificarClientes, eliminarClientes, listaPlanes, agregarPlanes, modificarPlanes, eliminarPlanes, listaEntregas

urlpatterns = [
    path("", Aplicacion),
    path('home/', inicio, name='home'),

    path('clientes/', listaClientes, name='clientes'),
    path('agregarClientes/', agregarClientes, name='agregarClientes'),
    path('modificarClientes/<id_cliente>', modificarClientes, name='modificarClientes'),
    path('eliminarClientes/<id_cliente>', eliminarClientes, name='eliminarClientes'),

    path('planes/', listaPlanes, name='planes'),
    path('agregarPlanes', agregarPlanes, name='agregarPlanes'),
    path('modificarPlanes/<id_plan>', modificarPlanes, name='modificarPlanes'),
    path('eliminarPlanes/<id_plan>', eliminarPlanes, name='eliminarPlanes'),

    path('entregas1/', listaEntregas.as_view(), name='entregas1'),


]
