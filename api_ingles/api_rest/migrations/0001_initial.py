# Generated by Django 2.2.4 on 2019-09-01 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('run', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='RUN')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('exam', models.CharField(choices=[('TOEIC', 'TOEIC Bridge'), ('ET', 'Examen Transversal')], max_length=20, verbose_name='Examen')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('hora_inicio', models.TimeField(verbose_name='Hora Inicio')),
                ('hora_fin', models.TimeField(verbose_name='Hora Fin')),
                ('sala', models.CharField(max_length=20, verbose_name='Sala')),
                ('proctor', models.CharField(max_length=255, verbose_name='Proctor')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Datos',
                'ordering': ['-fecha'],
            },
        ),
    ]