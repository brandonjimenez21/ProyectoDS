from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

# Modelo de Usuario con roles
class Usuario(AbstractUser):
    ADMIN = 'admin'
    DTH = 'dth'
    POSTULANTE = 'postulante'

    ROLES = [
        (ADMIN, 'Administrador'),
        (DTH, 'Director de Talento Humano'),
        (POSTULANTE, 'Postulante'),
    ]

    rol = models.CharField(max_length=20, choices=ROLES, default=POSTULANTE)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

# Modelo de Ofertas Laborales
class OfertaLaboral(models.Model):
    CARGOS = [
        ('UI/UX', 'Analista/Desarrollador UI/UX'),
        ('Back-End', 'Analista/Desarrollador Back-End'),
        ('Comercial', 'Analista Comercial'),
        ('Arquitecto', 'Arquitecto y Dueño de Producto'),
        ('Proyectos', 'Director de Proyectos Ágiles'),
        ('Lider', 'Líder de Equipo y Tecnología'),
        ('QA', 'Ingeniero de Calidad'),
    ]

    RANGOS = [
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
    ]

    titulo = models.CharField(max_length=255)
    tipo_cargo = models.CharField(max_length=50, choices=CARGOS)
    rango = models.CharField(max_length=20, choices=RANGOS)
    nivel_educativo = models.CharField(max_length=255)
    requerimientos = models.TextField()
    funciones = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    publicado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def clean(self):
        if self.publicado_por.rol != Usuario.DTH:
            raise ValidationError("Solo un Director de Talento Humano puede publicar ofertas laborales.")

# Modelo de Postulaciones a ofertas laborales
class Postulacion(models.Model):
    postulante = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': Usuario.POSTULANTE})
    oferta = models.ForeignKey(OfertaLaboral, on_delete=models.CASCADE)
    titulo_pregrado = models.FileField(upload_to='titulos/')
    titulo_posgrado = models.FileField(upload_to='titulos/', blank=True, null=True)
    hoja_vida = models.FileField(upload_to='hojas_vida/')
    motivo = models.TextField()
    fecha_postulacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['postulante', 'oferta'], name='unique_postulacion')
        ]