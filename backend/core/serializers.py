from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import OfertaLaboral, Postulacion

# Serializador para Usuarios
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'rol', 'first_name', 'last_name', 'telefono', 'direccion']

# Serializador para Ofertas Laborales
class OfertaLaboralSerializer(serializers.ModelSerializer):
    publicado_por = serializers.PrimaryKeyRelatedField(read_only=True)  # Ahora solo se muestra el ID del usuario

    class Meta:
        model = OfertaLaboral
        fields = '__all__'

# Serializador para Postulaciones
class PostulacionSerializer(serializers.ModelSerializer):
    postulante = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.filter(rol='postulante'))
    oferta = serializers.PrimaryKeyRelatedField(queryset=OfertaLaboral.objects.all())

    class Meta:
        model = Postulacion
        fields = '__all__'