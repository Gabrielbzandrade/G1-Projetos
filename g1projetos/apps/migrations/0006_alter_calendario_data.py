# Generated by Django 4.2 on 2023-11-27 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_perfil_padrinho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendario',
            name='data',
            field=models.TextField(max_length=16),
        ),
    ]
