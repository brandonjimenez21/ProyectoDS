from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario  # Importa tu modelo de usuario

class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "rol", "is_staff", "is_active")
    list_filter = ("rol", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
        ("Rol", {"fields": ("rol",)}),  # Asegúrate de que "rol" existe en tu modelo
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "is_staff", "is_active", "rol"),
        }),
    )
    search_fields = ("username", "email")
    ordering = ("username",)

admin.site.register(Usuario, CustomUserAdmin)  # Registra el modelo de usuario en el panel de admin