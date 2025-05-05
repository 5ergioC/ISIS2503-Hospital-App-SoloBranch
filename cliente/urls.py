from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('clientes/', views.cliente_list, name='clienteList'),
    path('clienteCreate/', csrf_exempt(views.cliente_create), name='clienteCreate'),
    path('clientesIntegridad/', views.cliente_integrity_check, name='clienteIntegrityCheck'),
    path('clientes/integridad/', views.verificar_integridad_view, name='verificarIntegridad'),
]