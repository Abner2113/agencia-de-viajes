from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.utils import timezone

# Create your models here.


# Descripción: Almacena información de clientes y sus preferencias.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    direccion = models.CharField(max_length=200)
    fecha_registro = models.DateField(auto_now_add=True)
    preferencias = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


# Descripción: Usuarios del sistema con autenticación completa y campos extendidos para empleados de la agencia.
class Empleado(AbstractUser):
    id = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to="empleados/perfil/", null=True, blank=True)
    cover = models.ImageField(upload_to="empleados/portada/", null=True, blank=True)
    about_me = models.TextField(blank=True)
    puesto = models.CharField(
        max_length=50,
        choices=[("Vendedor", "Vendedor"), ("Gerente", "Gerente")],
        default="Vendedor",
    )
    is_admin = models.BooleanField(default=False)
    fecha_contratacion = models.DateField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username


# Descripción: Aerolíneas, hoteles, tour operadores.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# Descripción: Ciudades o países turísticos.
class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre}, {self.pais}"


# Descripción: Vuelos, hoteles, excursiones.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


# Descripción: Vuelo + hotel + tours vendidos como un todo.
class Paquete(models.Model):
    nombre = models.CharField(max_length=100)
    productos = models.ManyToManyField(Producto)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


# Descripción: Registro de ventas con detalles de pago y empleado asignado.
class Reserva(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.SET_NULL, null=True, blank=True
    )
    paquete = models.ForeignKey(
        Paquete, on_delete=models.SET_NULL, null=True, blank=True
    )
    empleado = models.ForeignKey(
        Empleado, on_delete=models.SET_NULL, null=True, blank=True
    )
    fecha_reserva = models.DateField(null=False, blank=False)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(
        max_length=50,
        choices=[
            ("Efectivo", "Efectivo"),
            ("Tarjeta", "Tarjeta"),
            ("Transferencia", "Transferencia"),
        ],
        default="Efectivo",
    )
    estado = models.CharField(
        max_length=20,
        choices=[
            ("pendiente", "Pendiente"),
            ("confirmada", "Confirmada"),
            ("cancelada", "Cancelada"),
        ],
        default="pendiente",
    )


# Descripción: Llamadas, emails o recordatorios con clientes.
class Interaccion(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.SET_NULL, null=True, blank=True
    )
    empleado = models.ForeignKey(
        Empleado, on_delete=models.SET_NULL, null=True, blank=True
    )
    tipo = models.CharField(
        max_length=50,
        choices=[("Llamada", "Llamada"), ("Email", "Email"), ("Reunión", "Reunión")],
        default="Llamada",
    )
    fecha_interaccion = models.DateTimeField(default=timezone.now)
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tipo} con {self.cliente} por {self.empleado} el {self.fecha_interaccion.strftime('%Y-%m-%d %H:%M')}"


# Descripción: Comentarios y calificaciones de clientes sobre paquetes turísticos.
class Comentario(models.Model):
    paquete = models.ForeignKey(
        Paquete, on_delete=models.CASCADE, related_name="comentarios"
    )
    empleado = models.ForeignKey(
        Empleado, on_delete=models.SET_NULL, null=True, blank=True
    )
    texto = models.TextField()
    calificacion = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)], default=5
    )
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.empleado} en {self.paquete} ({self.calificacion}★)"
