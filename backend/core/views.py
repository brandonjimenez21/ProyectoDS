from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .models import OfertaLaboral, Postulacion
from .serializers import UsuarioSerializer, OfertaLaboralSerializer, PostulacionSerializer
from .permissions import EsAdministrador, EsDirectorTalentoHumano, EsPostulante

# Vista para Usuarios (solo Admin puede ver todos, pero los usuarios pueden ver su propia cuenta)
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [EsAdministrador]

    def get_queryset(self):
        user = self.request.user
        if user.rol == "admin":
            return get_user_model().objects.all()  # Admin ve todos los usuarios
        return get_user_model().objects.filter(id=user.id)  # Los usuarios ven solo su perfil

# Vista para Ofertas Laborales (solo DTH puede crear ofertas)
class OfertaLaboralViewSet(viewsets.ModelViewSet):
    queryset = OfertaLaboral.objects.all()
    serializer_class = OfertaLaboralSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [EsDirectorTalentoHumano()]
        return [permissions.AllowAny()]  # Cualquiera puede ver las ofertas

    def perform_create(self, serializer):
        serializer.save(publicado_por=self.request.user)  # Asignar el creador de la oferta

# Vista para Postulaciones (solo postulantes pueden postularse)
class PostulacionViewSet(viewsets.ModelViewSet):
    queryset = Postulacion.objects.all()
    serializer_class = PostulacionSerializer
    permission_classes = [EsPostulante]

    def get_queryset(self):
        return Postulacion.objects.filter(postulante=self.request.user)  # Filtrar para que cada usuario vea solo sus postulaciones

    def perform_create(self, serializer):
        serializer.save(postulante=self.request.user)  # Asignar automáticamente al usuario autenticado