from rest_framework import permissions

class EsAdministrador(permissions.BasePermission):
    """Permite acceso solo a administradores activos."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_active and getattr(request.user, 'rol', None) == 'admin'

class EsDirectorTalentoHumano(permissions.BasePermission):
    """Permite acceso a Directores de Talento Humano activos y Administradores."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_active and getattr(request.user, 'rol', None) in ['dth', 'admin']

class EsPostulante(permissions.BasePermission):
    """Permite acceso a postulantes activos y administradores."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_active and getattr(request.user, 'rol', None) in ['postulante', 'admin']