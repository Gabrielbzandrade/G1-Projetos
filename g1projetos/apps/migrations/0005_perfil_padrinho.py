# Generated by Django 4.2 on 2023-11-22 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_alter_perfil_data_nascimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='padrinho',
            field=models.TextField(default=0, max_length=300),
            preserve_default=False,
        ),
    ]