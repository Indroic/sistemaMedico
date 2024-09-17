import uuid

from django.db import models

from usuarios.models import Usuario



# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=100, unique=True)
    
    create_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    update_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.categoria


class Examen(models.Model):
    id = models.UUIDField(default=uuid.uuid1(), null=False, blank=False, primary_key=True)
    
    create_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    
    update_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    def upload_to(instance, filename):
        # obtiene la extension del archivo
        extension: str = filename.split('.')[-1]

        # obtiene el nombre del usuario
        
        usuario = instance.agregado_por.username

        
        # genera una cadena de caracteres para el nombre del archivo y elimina todos los "-" que tenga
        caracteres = str(uuid.uuid4()).replace('-', '')

        # crea el nuevo nombre
        nuevo_nombre = usuario + "." + caracteres + "." + extension

        # crea el nuevo nombre y reemplaza todos los espacios por "-"
        nuevo_nombre = str(usuario + "." + caracteres + "." + extension).replace(" ", "-")

        # retorna el nuevo nombre
        return "examenes/{0}/{1}/{2}".format(usuario, extension.upper(), nuevo_nombre)
    
    archivo = models.FileField(
        upload_to=upload_to, blank=False, null=False, unique=False
    )

    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, blank=False, null=False, unique=False
    )

    agregado_por = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, blank=False, null=False, unique=False
    )
    
    def __str__(self):
        return self.archivo + " - " + self.categoria.categoria + " - " + self.agregado_por.username
