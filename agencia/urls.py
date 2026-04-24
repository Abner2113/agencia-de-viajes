from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),

#---------CLIENTES---------
    path('clientes/', views.ClienteListaView.as_view(), name='clientes'),
    path('clientes/registrar/', views.ClienteCrearView.as_view(), name='registrar_cliente'),
    path('clientes/actualizar/<int:id>/', views.ClienteActualizarView.as_view(), name='actualizar_cliente'),
    path('clientes/eliminar/<int:id>/', views.ClienteEliminarView.as_view(), name='eliminar_cliente'),

#--------EMPLEADOS---------
    path('empleados/', views.EmpleadoListaView.as_view(), name='empleados'),
    path('empleados/registrar/', views.EmpleadoCrearView.as_view(), name='registrar_empleado'),
    path('empleados/actualizar/<str:id>/', views.EmpleadoActualizarView.as_view(), name='actualizar_empleado'),
    path('empleados/eliminar/<str:id>/', views.EmpleadoEliminarView.as_view(), name='eliminar_empleado'),

#---------PROVEEDORES---------
    path('proveedores/', views.ProveedorListaView.as_view(), name='proveedores'),
    path('proveedores/registrar/', views.ProveedorCrearView.as_view(), name='registrar_proveedor'),
    path('proveedores/actualizar/<int:id>/', views.ProveedorActualizarView.as_view(), name='actualizar_proveedor'),
    path('proveedores/eliminar/<int:id>/', views.ProveedorEliminarView.as_view(), name='eliminar_proveedor'),

#---------PRODUCTOS---------
    path('productos/', views.ProductoListaView.as_view(), name='productos'),
    path('productos/registrar/', views.ProductoCrearView.as_view(), name='registrar_producto'),
    path('productos/actualizar/<int:id>/', views.ProductoActualizarView.as_view(), name='actualizar_producto'),
    path('productos/eliminar/<int:id>/', views.ProductoEliminarView.as_view(), name='eliminar_producto'),

#--------DESTINOS---------
    path('destinos/', views.DestinoListaView.as_view(), name='destinos'),
    path('destinos/registrar/', views.DestinoCrearView.as_view(), name='registrar_destino'),
    path('destinos/actualizar/<int:id>/', views.DestinoActualizarView.as_view(), name='actualizar_destino'),
    path('destinos/eliminar/<int:id>/', views.DestinoEliminarView.as_view(), name='eliminar_destino'),

#--------PAQUETES---------
    path('paquetes/', views.PaqueteListaView.as_view(), name='paquetes'),
    path('paquetes/registrar/', views.PaqueteCrearView.as_view(), name='registrar_paquete'),
    path('paquetes/actualizar/<int:id>/', views.PaqueteActualizarView.as_view(), name='actualizar_paquete'),
    path('paquetes/eliminar/<int:id>/', views.PaqueteEliminarView.as_view(), name='eliminar_paquete'),

#--------RESERVAS---------
    path('reservas/', views.ReservaListaView.as_view(), name='reservas'),
    path('reservas/registrar/', views.ReservaCrearView.as_view(), name='registrar_reserva'),
    path('reservas/actualizar/<int:id>/', views.ReservaActualizarView.as_view(), name='actualizar_reserva'),
    path('reservas/eliminar/<int:id>/', views.ReservaEliminarView.as_view(), name='eliminar_reserva'),

#--------INTERACCIONES---------
    path('interacciones/', views.InteraccionListaView.as_view(), name='interacciones'),
    path('interacciones/registrar/', views.InteraccionCrearView.as_view(), name='registrar_interaccion'),
    path('interacciones/actualizar/<int:id>/', views.InteraccionActualizarView.as_view(), name='actualizar_interaccion'),
    path('interacciones/eliminar/<int:id>/', views.InteraccionEliminarView.as_view(), name='eliminar_interaccion'),
    
#--------LOGIN---------
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('acceso-denegado/', views.AccesoDenegadoView.as_view(), name='acceso_denegado'),

#--------DASHBOARD---------
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

#---------ROLES---------
    path('roles/', views.RolListaView.as_view(), name='roles'),
    path('roles/registrar/', views.RolCrearView.as_view(), name='registrar_rol'),
    path('roles/actualizar/<int:id>/', views.RolActualizarView.as_view(), name='actualizar_rol'),
    path('roles/eliminar/<int:id>/', views.RolEliminarView.as_view(), name='eliminar_rol'),

#--------COMENTARIOS---------
    path('paquetes/<int:id>/comentarios/', views.ComentarioListaView.as_view(), name='comentarios_paquete'),
    path('paquetes/<int:id>/comentarios/registrar/', views.ComentarioCrearView.as_view(), name='registrar_comentario'),
    path('comentarios/editar/<int:id>/', views.ComentarioActualizarView.as_view(), name='editar_comentario'),
    path('comentarios/eliminar/<int:id>/', views.ComentarioEliminarView.as_view(), name='eliminar_comentario'),

#--------REPORTES---------
    path('reportes/', views.ReportesView.as_view(), name='reportes'),
    path('reportes/exportar/excel/', views.ReportesExportExcelView.as_view(), name='exportar_excel'),
    path('reportes/exportar/pdf/', views.ReportesExportPDFView.as_view(), name='exportar_pdf'),
 
#--------CALENDARIO---------
    path('reservas/json/', views.ReservasJsonView.as_view(), name='reservas_json'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)