from django.contrib import admin

# Register your models here.
from persona.models import Docente, Asesor, Persona, Alumno


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    search_fields = ('cuil',)


@admin.register(Asesor)
class AsesorAdmin(admin.ModelAdmin):
    search_fields = ('cuil',)


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    search_fields = ('matricula',)
