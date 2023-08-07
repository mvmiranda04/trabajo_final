from django.db import models


class Persona(models.Model):
    dni = models.CharField(max_length=8, unique=True)
    apellido = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)

    class Meta:
        ordering = ('apellido',)

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s, %s' % (self.apellido, self.nombre)


class Docente(Persona):
    cuil = models.CharField(max_length=13)


class Asesor(Persona):
    cuil = models.CharField(max_length=13)
    # cvar = models.FileField(upload_to='personas/documentacion/', verbose_name='Cvar')


class Alumno(Persona):
    matricula = models.CharField(max_length=10, verbose_name='Matricula')
    email = models.CharField(max_length=200, verbose_name='Email')
    certificado_analitico = models.FileField(upload_to='archivos/documentacion_persona/', verbose_name='Certificado '
                                                                                                       'adjunto')
