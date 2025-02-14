from django.contrib import admin
from django.urls import path
from appips.views import *

urlpatterns = [   
 path('admin/', admin.site.urls),
 path('crear_usuario/', UsuarioCreate.as_view(), name='crear_usuario'),
 path('listar_usuarios/', buscar_usuario, name='listar_usuarios'),
 path('crear-registro/<str:numero_identificacion>/',crear_registro, name='crear_registro'),
 path('registro/<int:pk>/', DetalleRegistroView.as_view(), name='detalle_registro'),
 path('home/',home, name='home'), 
 #path('exportar-reporte/',exportar_registro_pacientes, name='exportar_reporte'),
 path('exportar-reporte/',generar_reporte_excel, name='exportar_reporte'),
]