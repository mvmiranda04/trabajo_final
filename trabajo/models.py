from django.db import models

# Create your models here.
from persona.models import Docente, Asesor, Alumno


class Estado(models.Model):
    INICIADO = "INIC"
    ENVIADOCSTF = "ENCS"

    ESTADO_CHOICES = [
        (INICIADO, "Proyecto Iniciado"),
        (ENVIADOCSTF, "Proyecto enviado CSTF"),
    ]

    descripcion = models.CharField(max_length=400)
    descripcion = models.CharField(
        max_length=4,
        choices=ESTADO_CHOICES,
        default=INICIADO,
    )
    tiempo_maximo_dias = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return f'{self.descripcion}'


class TrabajoFinal(models.Model):
    class Meta:
        verbose_name = 'Trabajo final'
        verbose_name_plural = 'Trabajos finales'

        ordering = ('fecha_presentacion',)

    descripcion = models.CharField(max_length=400)
    nota_director = models.FileField(upload_to='archivos/documentacion_trabajo/', verbose_name='Nota Director')
    fecha_presentacion = models.DateField(null=True, blank=True, verbose_name='Fecha Presentacion')
    director = models.ForeignKey(Docente, on_delete=models.PROTECT, related_name='trabajos_finales_director')
    co_director = models.ForeignKey(Docente, on_delete=models.PROTECT, related_name='trabajos_finales_co_irector')
    asesor = models.ForeignKey(Asesor, on_delete=models.PROTECT, related_name='trabajos_finales_asesor')
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, related_name='trabajos_finales_estados')

    def __str__(self):
        return f'{self.descripcion}'

class Integrante(models.Model):
    trabajo_final = models.ForeignKey(TrabajoFinal, on_delete=models.PROTECT,
                                      related_name='trabajos_finales_integrante')
    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT, related_name='trabajos_finales_integrante')
    fecha_alta_alumno = models.DateField(null=True, blank=True, verbose_name='Fecha Alta')
    fecha_baja_alumno = models.DateField(null=True, blank=True, verbose_name='Fecha Baja')

    def __str__(self):
        return f'{self.alumno}'


class ArchivoTrabajo(models.Model):
    PROYECTO_TRABAJO_FINAL = "PTF"
    BORRADOR_INFORME_FINAL = "BIF"
    BORRADOR_INFORME_MODIFICADO = "BIM"

    ARCHIVO_CHOICES = [
        (PROYECTO_TRABAJO_FINAL, "Proyecto Trabajo Final"),
        (BORRADOR_INFORME_FINAL, "Borrador Informe Final"),
        (BORRADOR_INFORME_MODIFICADO, "Borrador Informe Modificado"),
    ]

    trabajo_final = models.ForeignKey(TrabajoFinal, on_delete=models.PROTECT,
                                      related_name='trabajos_finales_archivos')
    fecha = models.DateField(null=True, blank=True, verbose_name='Fecha Presentacion Archivo')
    tipo_archivo = models.CharField(
        max_length=3,
        choices=ARCHIVO_CHOICES,
        default=PROYECTO_TRABAJO_FINAL,
    )
    archivo = models.FileField(upload_to='archivos/documentacion_trabajo/', verbose_name='Archivo adjunto', null=True,)

    def __str__(self):
        return f'{self.tipo_archivo}'


class DictamenTrabajo(models.Model):
    PROYECTO_TRABAJO_FINAL = "PTF"
    BORRADOR_INFORME_FINAL = "BIF"

    DICTAMENES_CHOICES = [
        (PROYECTO_TRABAJO_FINAL, "Proyecto Trabajo Final"),
        (BORRADOR_INFORME_FINAL, "Borrador Informe Final"),
    ]
    APROBADO = "A"
    OBSERVADO = "O"
    DESAPROBADO = "D"

    RESULTADO_CHOICES = [
        (APROBADO, "Aprobado"),
        (OBSERVADO, "Observado"),
        (DESAPROBADO, "Desaprobado"),
    ]

    trabajo_final = models.ForeignKey(TrabajoFinal, on_delete=models.PROTECT,
                                      related_name='trabajos_finales_dictamenes')
    fecha = models.DateField(null=True, blank=True, verbose_name='Fecha Dictamen')
    tipo_dictamen = models.CharField(
        max_length=4,
        choices=DICTAMENES_CHOICES,
        default=PROYECTO_TRABAJO_FINAL,
    )
    resultado_tipo_dictamen = models.CharField(
        max_length=1,
        choices=RESULTADO_CHOICES,
        default=APROBADO,
    )
    archivo = models.FileField(upload_to='archivos/documentacion_dictamen/', verbose_name='Archivo adjunto', null=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f'{self.tipo_dictamen}'


class Movimiento(models.Model):
    trabajo_final = models.ForeignKey(TrabajoFinal, on_delete=models.PROTECT,
                                      related_name='trabajos_finales_movimientos')
    fecha_inicio = models.DateField(null=True, blank=True, verbose_name='Fecha Inicio')
    fecha_fin = models.DateField(null=True, blank=True, verbose_name='Fecha Fin')
    fecha_vencimiento = models.DateField(null=True, blank=True, verbose_name='Fecha Vencimiento')
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, blank=True, related_name='movimientos_estados')