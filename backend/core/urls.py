from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import UsuarioViewSet, OfertaLaboralViewSet, PostulacionViewSet

# Router para generar las rutas automáticamente
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'ofertas', OfertaLaboralViewSet)
router.register(r'postulaciones', PostulacionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Incluye todas las rutas generadas automáticamente
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
