from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Cliente,
    Comentario,
    Empleado,
    Proveedor,
    Destino,
    Producto,
    Paquete,
    Reserva,
    Interaccion,
)


class EmpleadoAdmin(UserAdmin):
    model = Empleado
    list_display = ["email", "username", "puesto", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (
        (
            "Información de Agencia",
            {"fields": ("phone", "address", "puesto", "image", "cover", "about_me")},
        ),
    )


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Proveedor)
admin.site.register(Destino)
admin.site.register(Producto)
admin.site.register(Paquete)
admin.site.register(Reserva)
admin.site.register(Interaccion)
admin.site.register(Comentario)
