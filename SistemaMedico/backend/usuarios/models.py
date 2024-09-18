import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

def generar_nombre(instance, filename):
    """
    Genera un nombre unico para el archivo y lo retorna
    """


    # obtiene la extension del archivo
    extension = filename.split('.')[-1]
    # obtiene el nombre del usuario
    usuario = instance.username
    
    # genera una cadena de caracteres para el nombre del archivo y elimina todos los "-" que tenga
    caracteres = str(uuid.uuid4()).replace('-', '')
    # crea el nuevo nombre
    nuevo_nombre = usuario + "." + caracteres + "." + extension
    # retorna el nuevo nombre
    return "avatars/{0}".format(nuevo_nombre)

class Usuario(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, blank=False, null=False)
    
    ci = models.IntegerField(unique=True, blank=False, null=False, verbose_name="Cédula de Identidad")
    
    first_name = models.CharField(max_length=255, blank=False, null=False, verbose_name="Primer Nombre")
    
    last_name = models.CharField(max_length=255, blank=False, null=False, verbose_name="Primer Apellido")
    
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name="Correo Electronico")
    
    password = models.CharField(max_length=255, blank=False, null=False, verbose_name="Contraseña")
    
    create_at = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Fecha de Creacion")
    
    update_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name="Fecha de Actualizacion")
    
    avatar = ResizedImageField(upload_to=generar_nombre, null=True, blank=True, verbose_name="Avatar", size=[736, 736],  crop=['middle', 'center'], )
    
    REQUIRED_FIELDS = ['ci', 'first_name', 'last_name', 'email']
    
