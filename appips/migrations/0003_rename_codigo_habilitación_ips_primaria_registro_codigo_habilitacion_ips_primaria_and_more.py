# Generated by Django 5.1.1 on 2024-11-18 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appips', '0002_remove_usuario_edad_remove_usuario_fecha_registro_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro',
            old_name='codigo_habilitación_ips_primaria',
            new_name='codigo_habilitacion_ips_primaria',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='segundo_apellido',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='segundo_nombre',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo_identificacion',
            field=models.CharField(choices=[('AS', 'AS-Adulto Sin identificación'), ('CC', 'CC-Cedula de Ciudadanía'), ('CD', 'CD-Carnet Diplomático'), ('CE', 'CE-Cedula de Extranjería'), ('CN', 'CN-Certificado Nacido vivo'), ('DE', 'DE-Documento Extranjero'), ('MS', 'MS-Menor Sin identificación'), ('PA', 'PA-Pasaporte'), ('PE', 'PE-Permiso Especial de Permanencia'), ('PT', 'PT-Permiso por Protección Temporal'), ('RC', 'RC-Registro Civil'), ('SC', 'SC-Salvoconducto'), ('TI', 'TI-Tarjeta de Identidad')], max_length=2),
        ),
    ]
