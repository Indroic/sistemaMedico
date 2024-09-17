from django.contrib import admin
from .models import Examen, Categoria
# Register your models here.

class ExamenAdmin(admin.ModelAdmin):
    list_display = ('id', 'archivo', 'categoria', 'agregado_por', 'create_at', 'update_at')
    list_filter = ('create_at', 'update_at')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'create_at', 'update_at')
    list_filter = ('create_at', 'update_at')

admin.site.register(Examen, ExamenAdmin)
admin.site.register(Categoria, CategoriaAdmin)
