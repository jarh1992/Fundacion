# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 20:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tip_usu', models.CharField(choices=[('Super', 'Super'), ('Admin', 'Admin')], max_length=12)),
                ('Nom', models.CharField(max_length=40)),
                ('Ape', models.CharField(max_length=40)),
                ('Tip_id', models.CharField(choices=[('cc', 'cc'), ('ti', 'ti'), ('otro', 'otro')], max_length=12)),
                ('Num_id', models.CharField(max_length=10, unique=True)),
                ('Ciu', models.CharField(blank=True, max_length=60)),
                ('Tel', models.CharField(max_length=10)),
                ('Sex', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], max_length=12)),
                ('Dir', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Pass', models.CharField(max_length=16)),
                ('Foto', models.ImageField(upload_to='')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fundacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=40)),
                ('Num_id', models.CharField(max_length=10, unique=True)),
                ('Logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('Apellidos', models.CharField(blank=True, max_length=40)),
                ('Identificacion', models.CharField(max_length=10, unique=True)),
                ('Estado', models.CharField(choices=[('activo', 'activo'), ('inactivo', 'inactivo')], max_length=12)),
                ('Ciudad', models.CharField(blank=True, max_length=60)),
                ('Direccion', models.CharField(blank=True, max_length=200)),
                ('Sexo', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=12)),
                ('Fecha_ingreso', models.DateField(auto_now_add=True)),
                ('Telefono', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Foto', models.ImageField(upload_to='')),
            ],
        ),
    ]