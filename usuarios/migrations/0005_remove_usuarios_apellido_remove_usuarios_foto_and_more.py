# Generated by Django 4.2.7 on 2023-12-23 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_perfilestudiante_idperfilestudiante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='foto',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='nombre',
        ),
    ]
