# Generated by Django 5.1.1 on 2024-11-18 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appips', '0004_registro_unique_registro_por_usuario'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='registro',
            name='unique_registro_por_usuario',
        ),
        migrations.AlterField(
            model_name='registro',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appips.usuario', unique=True),
        ),
    ]
