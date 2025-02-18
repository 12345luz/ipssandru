# Generated by Django 5.1.1 on 2024-12-23 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appips', '0020_alter_ca_cervix_calidad_muestra_citologia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ca_colon',
            name='resultado_colonoscopia_tamizaje',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (2, '2 -Hallazgos compatibles con pólipos hiperplásicos'), (3, '3 -Hallazgos sugestivos de proceso preneoplásico'), (4, '4 -Hallazgos sugestivos de proceso neoplásico'), (5, '5 -Colonoscopia normal'), (6, '6 -Otros hallazgos'), (21, '21-Riesgo no evaluado')]),
        ),
        migrations.AlterField(
            model_name='ca_colon',
            name='resultado_prueba_sangre_oculta_mf',
            field=models.SmallIntegerField(choices=[(0, '20 -No aplica'), (4, '24 -Positivo'), (5, '25 -Negativo'), (6, '26 -No es posible determinar el resultado'), (21, '21-Riesgo no evaluado')]),
        ),
        migrations.AlterField(
            model_name='ca_mama',
            name='resultado_biopsia_mama',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (1, '1 -Benigna'), (2, '2 -Atípica (Indeterminada)'), (3, '3 -Malignidad sospechosa/probable'), (4, '4 -Maligna'), (5, '5 -No satisfactoria'), (21, '21-Riesgo no evaluado')]),
        ),
        migrations.AlterField(
            model_name='ca_mama',
            name='resultado_mamografia',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (1, '1 -BIRADS 0: necesidad de nuevo estudio imagenológico o mamograma previo para evaluación'), (2, '2 -BIRADS 1: negativo'), (3, '3 -BIRADS 2: hallazgos benignos'), (4, '4 -BIRADS 3: probablemente benigno'), (5, '5 -BIRADS 4: anormalidad sospechosa'), (6, '6 -BIRADS 5: altamente sospechoso de malignidad'), (7, '7 -BIRADS 6: malignidad por biopsia conocida'), (21, '21-Riesgo no evaluado')]),
        ),
        migrations.AlterField(
            model_name='ca_prostata',
            name='resultado_tacto_rectal',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (4, '4 -Próstata anormal'), (5, '5 -Próstata normal'), (21, '21-Riesgo no evaluado')]),
        ),
        migrations.AlterField(
            model_name='gestacion',
            name='acido_folico_preconcepcional',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (1, '1 -Sí'), (2, '2 -No'), (21, '21-Registro no evaluado')]),
        ),
        migrations.AlterField(
            model_name='gestacion',
            name='clasificacion_riesgo_gestacional',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (4, '4 -Alto riesgo'), (5, '5 -Bajo riesgo'), (21, '21-Riesgo no evaluado')]),
        ),
        migrations.AlterField(
            model_name='gestacion',
            name='gestante',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (1, '1 -Sí'), (2, '2 -No'), (21, '21-Riesgo no evaluado')]),
        ),
        migrations.AlterField(
            model_name='gestacion',
            name='suministro_acido_folico',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (1, '1 -Sí se suministra'), (16, '16-No se suministra por una tradición'), (17, '17-No se suministra por una condición de salud'), (18, '18-No se suministra por negación de la usuaria'), (20, '20-No se suministra por otras razones'), (21, '21-Registro no evaluado')]),
        ),
        migrations.AlterField(
            model_name='gestacion',
            name='suministro_carbonato_calcio',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (1, '1 -Sí se suministra'), (16, '16-No se suministra por una tradición'), (17, '17-No se suministra por una condición de salud'), (18, '18-No se suministra por negación de la usuaria'), (20, '20-No se suministra por otras razones'), (21, '21-Registro no evaluado')]),
        ),
        migrations.AlterField(
            model_name='gestacion',
            name='suministro_sulfato_ferroso',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (1, '1 -Sí se suministra'), (16, '16-No se suministra por una tradición'), (17, '17-No se suministra por una condición de salud'), (18, '18-No se suministra por negación de la usuaria'), (20, '20-No se suministra por otras razones'), (21, '21-Registro no evaluado')]),
        ),
        migrations.AlterField(
            model_name='riesgo_cardiovascular',
            name='clasificacion_riesgo_cardiovascular',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (4, '4 -Alto'), (5, '5 -Bajo'), (6, '6 -Moderado'), (21, '21-Riesgo no evaluado')]),
        ),
        migrations.AlterField(
            model_name='riesgo_cardiovascular',
            name='clasificacion_riesgo_metabolico',
            field=models.SmallIntegerField(choices=[(0, '0 - No aplica'), (4, '4 -Alto'), (5, '5 -Bajo'), (6, '6 -Moderado'), (21, '21-Riesgo no evaluado')]),
        ),
        migrations.AlterField(
            model_name='test_0_7',
            name='resultado_audicion_lenguaje',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (3, '3 -Sospecha de problemas de desarrollo'), (4, '4 -Riesgo de problemas de desarrollo'), (5, '5 -Desarrollo esperado para la edad'), (21, '21-Riesgo no evaluado')]),
        ),
        migrations.AlterField(
            model_name='test_0_7',
            name='resultado_motricidad_finoadaptativa',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (3, '3 -Sospecha de problemas de desarrollo'), (4, '4 -Riesgo de problemas de desarrollo'), (5, '5 -Desarrollo esperado para la edad'), (21, '21-Riesgo no evaluado')]),
        ),
        migrations.AlterField(
            model_name='test_0_7',
            name='resultado_motricidad_gruesa',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (3, '3 -Sospecha de problemas de desarrollo'), (4, '4 -Riesgo de problemas de desarrollo'), (5, '5 -Desarrollo esperado para la edad'), (21, '21-Riesgo no evaluado')]),
        ),
        migrations.AlterField(
            model_name='test_0_7',
            name='resultado_personal_social',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (3, '3 -Sospecha de problemas de desarrollo'), (4, '4 -Riesgo de problemas de desarrollo'), (5, '5 -Desarrollo esperado para la edad'), (21, '21-Riesgo no evaluado')]),
        ),
        migrations.AlterField(
            model_name='test_mayores_60',
            name='test_vejez',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (4, '4 -Sospecha de deterioro cognoscitivo'), (5, '5 -Normal'), (21, '21-Riesgo no evaluado')]),
        ),
        migrations.AlterField(
            model_name='toda_poblacion',
            name='resultado_antigeno_hepatitis_b',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (4, '4 -Reactivo'), (5, '5 -No reactivo'), (21, '21-Riesgo no evaluado')]),
        ),
        migrations.AlterField(
            model_name='toda_poblacion',
            name='resultado_prueba_vih',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica')]),
        ),
        migrations.AlterField(
            model_name='toda_poblacion',
            name='resultado_tamizaje_hepatitis_c',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica'), (4, '4 -Reactivo'), (5, '5 -No reactivo'), (21, '21-Riesgo no evaluado')]),
        ),
        migrations.AlterField(
            model_name='toda_poblacion',
            name='resultado_tamizaje_sifilis',
            field=models.SmallIntegerField(choices=[(0, '0 -No aplica')]),
        ),
        migrations.AlterField(
            model_name='tuberculosis',
            name='Resultado_baciloscopia',
            field=models.SmallIntegerField(choices=[(1, '1 -Negativa'), (2, '2 -Positiva'), (3, '3 -En proceso'), (4, '4 -No'), (21, '21-Riesgo no evaluado')]),
        ),
        migrations.AlterField(
            model_name='tuberculosis',
            name='Sintomatico_respiratorio',
            field=models.SmallIntegerField(choices=[(1, '1 -Sí'), (2, '2 -No'), (21, '21-Riesgo no evaluado')]),
        ),
    ]
