from django.contrib import admin
from .models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "create_at",
        "update_at",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_filter = ("create_at", "update_at")
    
    search_fields = ("username", "email", "ci", "id")

    fieldsets = (
        (None, {"fields": ("username", "avatar", "password")}),
        ("Informacion Personal", {"fields": ("first_name", "last_name", "ci","email")}),
        (
            "Seguridad",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )


admin.site.register(Usuario, UsuarioAdmin)
