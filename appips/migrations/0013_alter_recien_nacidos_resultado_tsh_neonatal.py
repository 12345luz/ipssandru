# Generated by Django 5.1.1 on 2024-12-05 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appips', '0012_alter_recien_nacidos_resultado_oximetria_pre_post_ductal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recien_nacidos',
            name='resultado_tsh_neonatal',
            field=models.SmallIntegerField(choices=[(0, '0-No aplica'), (4, '4-Alterado'), (5, '5-Normal'), (21, '21-Riesgo no evaluado')]),
        ),
    ]