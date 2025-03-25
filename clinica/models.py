from django.db import models
from django.contrib.auth.models import User


class Medico(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.username


class Paciente(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    historial_medico = models.TextField()
    doctor_asignado = models.ForeignKey(
        Medico, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
