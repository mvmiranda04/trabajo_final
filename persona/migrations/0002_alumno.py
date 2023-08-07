# Generated by Django 4.2.4 on 2023-08-03 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='persona.persona')),
                ('matricula', models.CharField(max_length=10, verbose_name='Matricula')),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('certificado_analitico', models.FileField(upload_to='personas/documentacion/', verbose_name='Certificado adjunto')),
            ],
            bases=('persona.persona',),
        ),
    ]