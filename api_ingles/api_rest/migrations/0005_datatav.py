# Generated by Django 2.2.4 on 2020-01-25 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0004_starrating'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataTAV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(max_length=12, verbose_name='RUN')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('asignatura', models.CharField(max_length=255, verbose_name='Asignatura')),
                ('seccion', models.CharField(max_length=255, verbose_name='Seccion')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('hora_inicio', models.CharField(max_length=5, verbose_name='Hora Inicio')),
                ('hora_fin', models.CharField(max_length=5, verbose_name='Hora Fin')),
                ('sala', models.CharField(max_length=255, verbose_name='Sala')),
                ('docente', models.CharField(max_length=255, verbose_name='Proctor')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'DataTAV',
                'verbose_name_plural': 'DataTAVs',
                'ordering': ['-created'],
            },
        ),
    ]
