from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    ADMIN = 'admin'
    USER = 'user'

    ROLES = [
        (ADMIN, 'Administrador'),
        (USER, 'Usuario Normal'),
    ]

    rol = models.CharField(max_length=10, choices=ROLES)

    groups = models.ManyToManyField(Group, related_name="usuario_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="usuario_permissions", blank=True)
