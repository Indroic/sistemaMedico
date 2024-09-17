from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'create_at', 'update_at')
    list_filter = ('create_at', 'update_at')

admin.site.register(Usuario, UsuarioAdmin)
