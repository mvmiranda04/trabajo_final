from django.contrib import admin

# Register your models here.
from trabajo.models import TrabajoFinal, Integrante, Estado, ArchivoTrabajo, DictamenTrabajo, Movimiento


@admin.register(TrabajoFinal)
class TrabajoFinalAdmin(admin.ModelAdmin):
    search_fields = ('descripcion',)


@admin.register(Integrante)
class IntegranteAdmin(admin.ModelAdmin):
    search_fields = ('descripcion',)


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    search_fields = ('descripcion',)


@admin.register(ArchivoTrabajo)
class ArchivoTrabajoAdmin(admin.ModelAdmin):
    search_fields = ('descripcion',)


@admin.register(DictamenTrabajo)
class DictamenTrabajoAdmin(admin.ModelAdmin):
    search_fields = ('tipo_dictamen',)


@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    search_fields = ('estado',)


