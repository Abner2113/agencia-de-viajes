from django import forms
from .models import (
    Cliente,
    Empleado,
    Proveedor,
    Producto,
    Destino,
    Paquete,
    Reserva,
    Interaccion,
    Comentario,
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group, Permission


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre completo"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "ejemplo@correo.com"}
            ),
            "telefono": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "10 dígitos"}
            ),
            "direccion": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Dirección"}
            ),
            "preferencias": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Preferencias del cliente",
                }
            ),
        }


class EmpleadoRegistroForm(UserCreationForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        label="Roles",
    )

    class Meta(UserCreationForm.Meta):
        model = Empleado
        fields = [
            "id",
            "username",
            "email",
            "phone",
            "address",
            "image",
            "cover",
            "puesto",
            "about_me",
            "groups",
        ]
        widgets = {
            "id": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "ID del empleado"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "ejemplo@correo.com"}
            ),
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre completo"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "10 dígitos"}
            ),
            "address": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Dirección"}
            ),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "cover": forms.FileInput(attrs={"class": "form-control"}),
            "about_me": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Descripción del empleado",
                }
            ),
            "puesto": forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Contraseña"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Confirmar contraseña"}
        )


# Formulario para ACTUALIZAR un empleado existente
class EmpleadoForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        label="Roles",
    )

    class Meta:
        model = Empleado
        fields = [
            "id",
            "email",
            "username",
            "phone",
            "address",
            "image",
            "cover",
            "about_me",
            "puesto",
            "groups",
        ]
        widgets = {
            "id": forms.HiddenInput(),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "ejemplo@correo.com"}
            ),
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre completo"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "10 dígitos"}
            ),
            "address": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Dirección"}
            ),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "cover": forms.FileInput(attrs={"class": "form-control"}),
            "about_me": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Descripción del empleado",
                }
            ),
            "puesto": forms.Select(attrs={"class": "form-control"}),
        }


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = [
            "nombre",
            "contacto",
            "tipo",
        ]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del proveedor"}
            ),
            "tipo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: Hotel, Aerolínea"}
            ),
            "contacto": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Contacto del proveedor, Gmail/telefono",
                }
            ),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "tipo", "proveedor", "destino", "precio_base"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del producto"}
            ),
            "tipo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tipo de producto (Hotel, Vuelo, Tour)",
                }
            ),
            "proveedor": forms.Select(attrs={"class": "form-control"}),
            "destino": forms.Select(attrs={"class": "form-control"}),
            "precio_base": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Precio base"}
            ),
        }


class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = ["nombre", "pais", "descripcion"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del destino"}
            ),
            "pais": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "País"}
            ),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }


class PaqueteForm(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = ["nombre", "productos", "precio_total", "activo"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del paquete"}
            ),
            "productos": forms.SelectMultiple(attrs={"class": "form-control"}),
            "precio_total": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Precio total"}
            ),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            "cliente",
            "paquete",
            "empleado",
            "fecha_reserva",
            "precio_venta",
            "metodo_pago",
            "estado",
        ]
        widgets = {
            "cliente": forms.Select(attrs={"class": "form-control"}),
            "paquete": forms.Select(attrs={"class": "form-control"}),
            "empleado": forms.Select(attrs={"class": "form-control"}),
            "fecha_reserva": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "precio_venta": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Precio de venta"}
            ),
            "metodo_pago": forms.Select(attrs={"class": "form-control"}),
            "estado": forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True
            if hasattr(field, "empty_label"):
                field.empty_label = None


class InteraccionForm(forms.ModelForm):
    class Meta:
        model = Interaccion
        fields = ["cliente", "empleado", "tipo", "fecha_interaccion", "notas"]
        widgets = {
            "cliente": forms.Select(attrs={"class": "form-control"}),
            "empleado": forms.Select(attrs={"class": "form-control"}),
            "tipo": forms.Select(attrs={"class": "form-control"}),
            "fecha_interaccion": forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={"class": "form-control", "type": "datetime-local"},
            ),
            "notas": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Detalle de la interacción...",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["fecha_interaccion"].input_formats = ["%Y-%m-%dT%H:%M"]


class EmpleadoLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "correo@ejemplo.com"}
        ),
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "*********"}
        ),
    )


class RolForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.select_related("content_type").filter(
            content_type__app_label__in=["agencia", "auth"],
            content_type__model__in=[
                "cliente",
                "empleado",
                "proveedor",
                "producto",
                "destino",
                "paquete",
                "reserva",
                "interaccion",
                "comentario",
                "group",  # ← group es el modelo de roles
            ],
        ),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        label="Permisos",
    )

    class Meta:
        model = Group
        fields = ["name", "permissions"]
        labels = {"name": "Nombre del rol"}
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Vendedor, Gerente...",
                }
            ),
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["texto", "calificacion"]
        widgets = {
            "texto": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Escribe tu comentario sobre este paquete...",
                }
            ),
            "calificacion": forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            "texto": "Comentario",
            "calificacion": "Calificación (estrellas)",
        }


class ReservaFiltroForm(forms.Form):
    fecha_desde = forms.DateField(
        required=False,
        label="Fecha desde",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
    fecha_hasta = forms.DateField(
        required=False,
        label="Fecha hasta",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
    paquete = forms.CharField(
        required=False,
        label="Paquete / Destino",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Buscar por paquete..."}
        ),
    )
    empleado = forms.ModelChoiceField(
        queryset=Empleado.objects.all(),
        required=False,
        empty_label="Todos los colaboradores",
        label="Colaborador",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    estado = forms.ChoiceField(
        choices=[
            ("", "Todos los estados"),
            ("pendiente", "Pendiente"),
            ("confirmada", "Confirmada"),
            ("cancelada", "Cancelada"),
        ],
        required=False,
        label="Estado",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
