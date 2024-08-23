# Generated by Django 5.1 on 2024-08-16 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('fecha_Creacion', models.DateField(auto_now=True)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=50)),
            ],
        ),
    ]
