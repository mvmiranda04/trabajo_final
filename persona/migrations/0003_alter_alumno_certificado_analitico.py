# Generated by Django 4.2.4 on 2023-08-03 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_alumno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='certificado_analitico',
            field=models.FileField(upload_to='archivos/documentacion_persona/', verbose_name='Certificado adjunto'),
        ),
    ]