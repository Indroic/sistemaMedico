import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from usuarios.models import Usuario

# Create your models here.
class Especialidad(models.Model):
    especialidad = models.CharField(max_length=100, unique=True)
    
    create_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    update_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.especialidad

class Medico(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False, unique=False)
    
    apellido = models.CharField(max_length=100, blank=False, null=False, unique=False)
    
    telefono = PhoneNumberField(blank=False, null=False, unique=False)
    
    institucion = models.CharField(max_length=100, blank=False, null=False, unique=False)
    
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, blank=False, null=False, unique=False)
    
    agregado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=False, null=False, unique=False)
    
    id = models.UUIDField(default=uuid.uuid4(), null=False, blank=False, primary_key=True)
    
    create_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    
    update_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    
    def __str__(self):
        return self.nombre + " " + self.apellido + " - " + self.institucion + " - " + self.especialidad.especialidad