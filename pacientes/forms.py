from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['id_pac', 'nombre_pac', 'apellido_pac', 'fecha_nacimiento', 'telefono_pac', 'direccion_pac', 'correo_pac', 'fecha_registro']
        labels = {
            'id_pac': 'ID del Paciente',
            'nombre_pac': 'Nombre',
            'apellido_pac': 'Apellido',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'telefono_pac': 'Teléfono',
            'direccion_pac': 'Dirección',
            'correo_pac': 'Correo Electrónico',
            'fecha_registro': 'Fecha de Registro',
        }
        widgets = {
            'id_pac': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_pac': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_pac': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'telefono_pac': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_pac': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_pac': forms.EmailInput(attrs={'class': 'form-control'}),
            'fecha_registro': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }