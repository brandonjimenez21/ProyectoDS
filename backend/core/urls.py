from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UsuarioViewSet, OfertaLaboralViewSet, PostulacionViewSet

# Router para generar las rutas automáticamente
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'ofertas', OfertaLaboralViewSet)
router.register(r'postulaciones', PostulacionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Agregar las rutas de la API
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
]
