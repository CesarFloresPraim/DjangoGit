from django.db import models
from django import forms
from .models import Administrador, Ventas, IncentivosDiarios

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Administrador
        TIPOS_USUARIOS = (
            ('Administrador', 'Administrador'),
            ('Tecnico', 'Tecnico'),
        )
        fields = [
            'usuario',
            'contrasenia1',
            'email',
            'celular',
            'hora_entrada',
            'salario',
            'tipo'
        ]

        labels = {
            'usuario': 'Usuario',
            'contrasenia1': 'Contraseña',
            'email': 'Email',
            'celular': 'Celular',
            'hora_entrada': 'Hora de entrada y salario',
            'tipo': 'Tipo'
        }


        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'input96', 'placeholder': 'Escribir Usuario'}),
            'contrasenia1': forms.PasswordInput(attrs={'class': 'input45', 'placeholder': 'Escribir Contraseña'}),
            'email': forms.EmailInput(attrs={'class': 'input96', 'placeholder': 'Escribir Email'}),
            'celular': forms.TextInput(attrs={'class': 'input96', 'placeholder': 'Escribir Celular'}),
            'hora_entrada': forms.DateInput(attrs={'class': 'input45', 'placeholder': ' Hora: HH:MM'}),
            'salario': forms.TextInput(attrs={'class': 'input45', 'placeholder': 'Salario'}),
            'tipo': forms.Select(attrs={'class': 'input96'}, choices=TIPOS_USUARIOS)
        }

class VentaNuevaForm(forms.ModelForm):

    class Meta:
        METODOS_DE_PAGO_CHOICES = (
            ('Tarjeta', 'Tarjeta'),
            ('Efectivo', 'Efectivo'),
        )

        model = Ventas
        fields = [
            'cantidad',
            'descripcion',
            'precio',
            'costo',
            'metodo_de_pago'
        ]

        widgets = {
            'cantidad': forms.NumberInput(attrs={'class': 'input_ajuste', 'placeholder': 'Cantidad'}),
            'descripcion': forms.TextInput(attrs={'class': 'input_ajuste', 'placeholder': 'Desripcion'}),
            'precio': forms.NumberInput(attrs={'class': 'input_ajuste', 'placeholder': 'Precio'}),
            'costo': forms.NumberInput(attrs={'class': 'input_ajuste', 'placeholder': 'Costo'}),
            'metodo_de_pago': forms.Select(attrs={'class':'input_ajuste'}, choices=METODOS_DE_PAGO_CHOICES)
        }
