from django.db import models

# Create your models here.
class Paciente(models.Model):
    id_pac = models.PositiveIntegerField()
    nombre_pac = models.CharField(max_length=50)
    apellido_pac = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    telefono_pac = models.CharField(max_length=15)
    direccion_pac = models.CharField(max_length=100)
    correo_pac = models.EmailField(max_length=100)
    fecha_registro = models.DateTimeField()

    def __str__(self):
        return f"Paciente: {self.nombre_pac} {self.apellido_pac}"

