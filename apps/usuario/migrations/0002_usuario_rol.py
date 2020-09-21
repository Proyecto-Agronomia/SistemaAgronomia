# Generated by Django 2.2.6 on 2020-09-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('ADM', 'Administrador'), ('EST', 'Estudiante'), ('DOC', 'Profesor')], default='EST', max_length=3),
        ),
    ]
