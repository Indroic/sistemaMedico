import uuid
from django.db import models

class BaseModel(models.Model):
    
    id = models.UUIDField(default=uuid.uuid1(), null=False, blank=False, primary_key=True)
    
    create_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    
    update_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    

