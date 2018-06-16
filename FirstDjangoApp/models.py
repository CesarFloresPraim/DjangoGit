from django.db import models
from djmoney.models.fields import MoneyField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.forms import forms
import datetime
# Create your models here.

class Administrador(models.Model):
    TIPOS_USUARIOS = (
        ('Administrador', 'Administrador'),
        ('Tecnico', 'Tecnico'),
    )
    usuario = models.CharField(max_length=25,db_column='usuario', primary_key=True)
    contrasenia1 = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    celular = models.CharField(max_length=15)
    salario = models.IntegerField(default=0)
    hora_entrada = models.TimeField(null=True, blank=True)
    tipo = models.CharField(max_length=25, choices=TIPOS_USUARIOS, default='Tecnico')
    dias_laborales = models.IntegerField(null=False, validators=[MaxValueValidator(7), MinValueValidator(1)])
    fecha_ultimo_pago = models.DateField(auto_now_add=True, null=False)


    def __str__(self):
        return self.usuario
class PagoEmpleados(models.Model):
    usuario = models.CharField(max_length=25)
    cantidad_pago = models.IntegerField(null=False)
    fecha_pago= models.DateField(auto_now_add=True, null=False)


class HoraSesion(models.Model):
    usuario = models.CharField(max_length=25)
    hora_entrada = models.TimeField(null=False, blank=False)
    hora_sesion = models.TimeField(null=False)
    cantidad_incentivo = models.IntegerField(null=False)
    fecha_sesion = models.DateField(auto_now_add=True, null=False)


class Articulos(models.Model):
    descripcion = models.CharField(max_length=50, null=False, blank=False, primary_key=True)
    precio = models.IntegerField(default=0)
    costo = models.IntegerField(default=0)
    comision_empleado = models.IntegerField(default=0)
    objetivo_venta = models.IntegerField(default=0)

    def __str__(self):
        return self.descripcion

class IncentivosDiarios(models.Model):
    dia = models.CharField(max_length=10, null=False, blank=False, primary_key=True)
    bono_puntualidad = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.dia

class Ventas(models.Model):

    METODOS_DE_PAGO_CHOICES = (
        ('Tarjeta', 'Tarjeta'),
        ('Efectivo', 'Efectivo'),
    )

    fecha = models.DateTimeField(auto_now_add=True, blank=False)
    cantidad = models.IntegerField(null=False, blank=False)
    descripcion = models.CharField(max_length=50, null=False, blank=False, default='no_nombre')
    precio = MoneyField(max_digits=10, decimal_places=2, default_currency='MXN')
    costo = models.IntegerField(null=False, blank=False)
    metodo_de_pago = models.CharField(max_length=25, choices=METODOS_DE_PAGO_CHOICES)
    realizada_por = models.CharField(max_length=25, null=True, default='Otro Tecnico')

    def VentaMostrar(self):
        cadena = "{0} {1} el {2}"
        return cadena.format(self.cantidad, self.descripcion, self.fecha)

    def __str__(self):
        return self.VentaMostrar()

"""
class Alumno(models.Model):
    ApellidoPaterno = models.CharField(max_length=35)
    ApellidoMaterno = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=35)
    CURP = models.CharField(max_length=35)
    FechaNacimeinto = models.DateField()
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()

class Curso(models.Model):
    Nombre = models.CharField(max_length=50)
    Creditos = models.PositiveIntegerField()
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return "{0} ({1})".format(self.Nombre, self.Creditos)


class Matricula(models.Model):
    Alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
    Curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    FechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Alumno, self.Curso.Nombre)
"""
