# Generated by Django 5.1.4 on 2025-01-04 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0005_caracteristicas_documentacao_imagens_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastrocliente',
            name='email',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
