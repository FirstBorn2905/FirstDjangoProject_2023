from django.contrib import admin
from .models import Personal, Solicitud, ReporteVentas

# Register your models here.
admin.site.register(Personal)
admin.site.register(Solicitud)
admin.site.register(ReporteVentas)
