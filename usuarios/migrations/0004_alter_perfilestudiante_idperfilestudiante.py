# Generated by Django 4.2.7 on 2023-11-25 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_perfilcoordinador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilestudiante',
            name='idPerfilEstudiante',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
