from django.contrib import admin
from .models import Medico, Especialidad

class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'especialidad', 'create_at', 'update_at')
    list_filter = ('create_at', 'update_at')
    
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'telefono', 'institucion', 'especialidad', 'agregado_por', 'create_at', 'update_at')
    list_filter = ('create_at', 'update_at')
    
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Medico, MedicoAdmin)
