# Generated by Django 5.1.4 on 2025-01-27 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0011_alter_cadastrocliente_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caracteristicas',
            name='cliente',
        ),
    ]
