import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    id = models.UUIDField(default=uuid.uuid1(), primary_key=True)
    
    ci = models.IntegerField(unique=True, blank=False, null=False)
    
    create_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    
    update_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    
    REQUIRED_FIELDS = ['ci', 'first_name', 'last_name', 'email']
    
