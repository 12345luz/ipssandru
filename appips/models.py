import unicodedata
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.db.models import UniqueConstraint

# Modelo de BD
class Usuario(models.Model):

    CODIGO_NIVEL_EDUCATIVO_CHOICES = [
        (1, "Preescolar"),
        (2, "Básica Primaria"),
        (3, "Básica Secundaria"),
        (4, "Media Académica o Clásica"),
        (5, "Media Técnica (Bachillerato Técnico)"),
        (6, "Normalista"),
        (7, "Técnica Profesional"),
        (8, "Tecnológica"),
        (9, "Profesional"),
        (10, "Especialización"),
        (11, "Maestría"),
        (12, "Doctorado"),
        (13, "Ninguno"),
    ]

    #Tipo de identificación
    TIPO_IDENTIFICACION_CHOICES=[
    ("AS","AS-Adulto Sin identificación"),
    ("CC","CC-Cedula de Ciudadanía"),
    ("CD","CD-Carnet Diplomático"),
    ("CE","CE-Cedula de Extranjería"),
    ("CN","CN-Certificado Nacido vivo"),
    ("DE","DE-Documento Extranjero"),
    ("MS","MS-Menor Sin identificación"),
    ("PA","PA-Pasaporte"),
    ("PE","PE-Permiso Especial de Permanencia"),
    ("PT","PT-Permiso por Protección Temporal"),
    ("RC","RC-Registro Civil"),
    ("SC","SC-Salvoconducto"),
    ("TI","TI-Tarjeta de Identidad")
    ]

    #Tipo de genero
    SEXO_CHOICES=[
        ("F","Femenino"),
        ("M","Masculino")
    ]

    #Código de pertenencia etnica
    CODIGO_PERTENENCIA_CHOICES = [
        (1, 'Indígena'),
        (2, 'ROM(gitano)'),
        (3, 'Raizal(archipiélago de San Andrés y Providencia)'),
        (4, 'Palanquero de San Basilio'),
        (5, 'Negro(a) Mulato(a) Afrocolombiano(a) o Afro descendiente'),
        (6,"Ninguna de las anteriores"),
        (7,"Otro")
    ]

    #Codigo País
    CODIGO_PAIS_CHOICES=[
        (170,"COLOMBIA")  
    ]

    #Codigo de ocupación
    CODIGO_OCUPACION_CHOICES=[
        (9611, 'Recolectores de basura y material reciclable'),
        (9612, 'Clasificadores de desechos'),
        (9613, 'Barrenderos y afines'),
        (9621, 'Mensajeros, mandaderos, maleteros y repartidores'),
        (9622, 'Personas que realizan trabajos varios'),
        (9624, 'Acarreadores de agua y recolectores de leña'),
        (9625, 'Recolectores de dinero y surtidores de máquinas de venta automática'),
        (9626, 'Lectores de medidores'),
        (9629, 'Otras ocupaciones elementales no clasificadas en otros grupos primarios'),
        (9998, 'Jubilado, desempleado, ama de casa, estudiante, dedicación al hogar, menor de edad'),
        (9999, 'No informa'),
        ]
    
    tipo_identificacion = models.CharField(max_length=2, choices=TIPO_IDENTIFICACION_CHOICES)
    numero_identificacion = models.CharField(
        max_length=18,
        primary_key=True,
        validators=[RegexValidator(regex='^\d+$', message='El número de identificación debe contener solo dígitos.')])
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30, blank=True, null=True)
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    codigo_pertenencia_etnica = models.SmallIntegerField(choices=CODIGO_PERTENENCIA_CHOICES)
    codigo_ocupacion = models.SmallIntegerField(choices=CODIGO_OCUPACION_CHOICES)
    codigo_pais = models.SmallIntegerField(choices=CODIGO_PAIS_CHOICES)
    codigo_nivel_educativo = models.SmallIntegerField(choices=CODIGO_NIVEL_EDUCATIVO_CHOICES)

    def clean_text(self, text):
        """
        Convierte el texto a mayúsculas, elimina caracteres especiales y tildes.
        """
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
        return text.upper()
    
    def clean(self):
        """
        Validar que si el país es 170, el tipo de documento no sea uno de los restringidos.
        """
        if self.codigo_pais == 170 and self.tipo_identificacion in ['CE', 'PA', 'CD', 'PE', 'SC', 'DE']:
            raise ValidationError(
                {
                    'tipo_identificacion': 'El tipo de identificación no puede ser CE, PA, CD, PE, SC o DE si el país es Colombia (170).',
                    'codigo_pais': 'El país no puede ser Colombia(170) si el tipo de identificación es CE, PA, CD, PE, SC o DE.',
                }
            )
        
    def save(self, *args, **kwargs):
        # Validar antes de guardar
        self.clean()

        # Transformar los datos al formato deseado
        if self.primer_apellido:
            self.primer_apellido = self.clean_text(self.primer_apellido)
        if self.segundo_apellido:
            self.segundo_apellido = self.clean_text(self.segundo_apellido)
        if self.primer_nombre:
            self.primer_nombre = self.clean_text(self.primer_nombre)
        if self.segundo_nombre:
            self.segundo_nombre = self.clean_text(self.segundo_nombre)

        super().save(*args, **kwargs)
class Registro(models.Model):
    consecutivo_registro = models.AutoField(primary_key=True)
    tipo_registro = models.SmallIntegerField(default=2)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    codigo_habilitacion_ips_primaria = models.BigIntegerField(default=528380048301)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['id_usuario'], name='unique_registro_por_usuario')
        ]

    def __str__(self):
        return f"{self.consecutivo_registro} - {self.tipo_registro} - {self.id_usuario}"

#Programas

# Tabla agudeza_visual
class AgudezaVisual(models.Model):

    OPCIONES_CHOICES = [ 
        (0 ,"0 -No aplica"),
        (3 ,"3 -Menor o igual a 20/20 normal" ),
        (4 ,"4 -Entre 20/25 y 20/40"),
        (5 ,"5 -Mayor o igual de 20/50 hasta 1200 anormal"),
        (6 ,"6 -Cuenta dedos" ),
        (7 ,"7 -Percepción de bultos" ),
        (8 ,"8 -Proyección y percepción de luz "),
        (9 ,"9 -No percibe luz"),
        (21 ,"21-Riesgo no evaluado")
   ]
    consecutivo_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)  # Se especifica on_delete
    agudeza_visual_lejana_ojo_izquierdo = models.SmallIntegerField(choices=OPCIONES_CHOICES, default=0)
    agudeza_visual_lejana_ojo_derecho = models.SmallIntegerField(choices=OPCIONES_CHOICES, default=0) 
    fecha_valoracion_agudeza_visual = models.DateField()

    def __str__(self):
        return f"Agudeza visual para registro {self.consecutivo_registro}"

# Tabla anticoncepcion
class Anticoncepcion (models.Model):
  
    OPCIONES_CHOICES = [ 

    (0 ,"0 -No aplica"),
    (1 ,"1 -Dispositivo intrauterino"),
    (2 ,"2 -Dispositivo intrauterino y preservativo"),
    (3 ,"3 -Implante subdérmico"),
    (4 ,"4 -Implante subdérmico y preservativo"),
    (5 ,"5 -Oral"),
    (6 ,"6 -Oral y preservativo"),
    (7 ,"7 -Inyectable mensual"),
    (8 ,"8 -Inyectable mensual y preservativo "),
    (9 ,"9 -Inyectable trimestral"),
    (10,"10-Inyectable trimestral y preservativo"),
    (11,"11-Emergencia"),
    (12,"12-Emergencia y preservativo"),
    (13,"13-Esterilización"),
    (14,"14-Esterilización y preservativo"),
    (15,"15-Preservativo"),
    (16,"16-No se suministra por una tradición"),
    (17,"17-No se suministra por una condición de salud"),
    (18,"18-No se suministra por negación de la usuaria"),
    (20,"20-No se suministra por otras razones"),
    (21,"21-Registro no evaluado")]

    consecutivo_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    fecha_atencion_asesoria_anticoncep = models.DateField() 
    suministro_metodo_anticoceptivo =models.SmallIntegerField(choices=OPCIONES_CHOICES) 
    fecha_sumistro_ant = models.DateField() 
  
# Tabla ca_cervix
class Ca_Cervix (models.Model):

    OPCIONES_CHOICES = [ 

        (0,"20 -No aplica"),
        (6,"6 -Sí, se realizó tratamiento ablativo"),
        (7,"7 -Sí, se realizó tratamiento de escisión"),
        (8,"8 -Sí, se realizó tratamiento homologable a ablativo o de escisión"),
        (9,"9 -No se realizó ablación, escisión, ni tratamiento homologable, se requiere de otro procedimiento"),
        (10,"10-No se realizó ablación ni escisión por otras razones"),
        (21,"21-Registro no evaluado")]
    

    OPCIONES_CHOICES_TAM =[(0,"0 -No aplica"),
        (1,"1 -Citología cérvico uterina"),
        (2,"2 -Prueba ADN – VPH"),
        (3,"3 -Técnica de inspección visual"),
        (4,"4 -Prueba ADN-VPH y citología cérvico uterina"),
        (16,"6-No se realiza por una tradición"),
        (17,"7-No se realiza por una condición de salud "),
        (18,"8-No se realiza por negación de la usuaria "),
        (19,"9-No se realiza por tener datos de contacto de la usuaria no actualizados"),
        (20,"0-No se realiza por otras razones"),
        (21,"1-Riesgo no evaluado")]
    
    OPCIONES_CHOICES_RES=[(0,"0  - No aplica"),
        (1,"1  - ASC-US (células escamosas atípicas de significado indeterminado)"),
        (2,"2  - ASC-H (células escamosas atípicas, de significado indeterminado sugestivo de LEI de alto grado"),
        (3,"3  - Lesión intraepitelial escamosa (LEI) de bajo grado- HPV (NIC I) (LEI BG)"),
        (4,"4  - Lesión intraepitelial escamosa (LEI) de alto grado (NIC II-III CA INSITU) (LEI AG)"),
        (5,"5  - Lesión intraepitelial escamosa de alto grado sospechosa de infiltración"),
        (6,"6  - Carcinoma de células escamosas (Escamocelular)"),
        (7,"7  - Células endocervicales atípicas sin ningún otro significado"),
        (8,"8  - Células endometriales atípicas sin ningún otro significado"),
        (9,"9  - Células glandulares atípicas sin ningún otro significado"),
        (10,"10 - Células endocervicales atípicas sospechosas de neoplasia"),
        (11,"11 - Células endometriales atípicas sospechosas de neoplasia"),
        (12,"12 - Células glandulares atípicas sospechosas de neoplasia"),
        (13,"13 - Adenocarcinoma endocervical in situ"),
        (14,"14 - Adenocarcinoma endocervical"),
        (15,"15 - Adenocarcinoma endometrial"),
        (16,"16 - Otras neoplasias"),
        (17,"17 - Negativa para lesión intraepitelial o neoplasia"),
        (18,"18 - Inadecuada para lectura"),
        (19,"19 - Positivo "),
        (20,"20 - Negativo"),
        (21,"21 -Riesgo no evaluado")]
    
    OPCIONES_CHOICES_CAL=[(0,"0 -No aplica"),
        (1,"1 -Satisfactoria Zona de Transformación Presente"),
        (2,"2 -Satisfactoria Zona de Transformación Ausente"),
        (3,"3 -Insatisfactoria"),
        (4,"4 -Rechazada"),
        (999,"999-No se tiene el dato")]
    
    OPCIONES_CHOICES_RES_BIO=[(0 ,"0 -No aplica"),
        (1 ,"1 -Negativo para neoplasia "),
        (3 ,"3 -NIC de bajo grado (NIC I)"),
        (4 ,"4 -NIC de alto grado: (NIC II - NIC III) "),
        (5 ,"5 -Neoplasia micro infiltrante: escamocelular o adenocarcinoma"),
        (6 ,"6 -Neoplasia Infiltrante: escamocelular o adenocarcinoma"),
        (21,"21-Riesgo no evaluado")]

    consecutivo_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    tratamiento_ablativo_escision=models.SmallIntegerField(choices=OPCIONES_CHOICES)  
    tamizaje_cancer_cuello_uterino =models.SmallIntegerField(choices=OPCIONES_CHOICES_TAM)  
    fecha_tamizaje_cancer_cuello_uterino = models.DateField()  
    resultado_tamizaje_cancer_cuello_uterino =models.SmallIntegerField(choices=OPCIONES_CHOICES_RES) 
    calidad_muestra_citologia =models.SmallIntegerField(choices=OPCIONES_CHOICES_CAL)
    codigo_habilitacion_ips_cancer_cuello_uterino= models.BigIntegerField() #-- Código de habilitación de la IPS
    fecha_colposcopia = models.DateField()  #-- Fecha de colposcopia
    fecha_biopsia_cervicouterina = models.DateField()  #Fecha de biopsia cervicouterina
    resultado_biopsia_cervicouterina =models.SmallIntegerField(choices=OPCIONES_CHOICES_RES_BIO)  # Resultado de la biopsia
 
#-- Tabla ca_colon
class Ca_Colon (models.Model):
  
    OPCIONES_CHOICES=[(0,"20 -No aplica"),
    (4,"24 -Positivo"),
    (5,"25 -Negativo"),
    (6,"26 -No es posible determinar el resultado"),
    (21,"21-Riesgo no evaluado")]

    OPCIONES_CHOICES_TAM=[
    (0,"0 -No aplica"),
    (2,"2 -Hallazgos compatibles con pólipos hiperplásicos"),
    (3,"3 -Hallazgos sugestivos de proceso preneoplásico"),
    (4,"4 -Hallazgos sugestivos de proceso neoplásico"),
    (5,"5 -Colonoscopia normal"),
    (6,"6 -Otros hallazgos"),
    (21,"21-Riesgo no evaluado")]

    consecutivo_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    resultado_prueba_sangre_oculta_mf =models.SmallIntegerField(choices=OPCIONES_CHOICES)  
    resultado_colonoscopia_tamizaje =models.SmallIntegerField(choices=OPCIONES_CHOICES_TAM)  #Resultado de colonoscopia tamizaje
    fecha_colonoscopia_tamizaje = models.DateField()   #Fecha de colonoscopia tamizaje
    fecha_prueba_sangre_oculta = models.DateField()   

# Tabla ca_prostata
class Ca_Prostata (models.Model):
  
    OPCIONES_CHOICES=[
    (0, "0 -No aplica"),
    (4, "4 -Próstata anormal"),
    (5, "5 -Próstata normal"),
    (21,"21-Riesgo no evaluado")]

    consecutivo_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    resultado_tacto_rectal = models.SmallIntegerField(choices=OPCIONES_CHOICES)  # Resultado del tacto rectal
    fecha_tacto_rectal = models.DateField()  # Fecha del tacto rectal
    fecha_toma_psa = models.DateField()  # Fecha de toma de PSA
    resultado_psa = models.DecimalField(max_digits=4, decimal_places=2)# Resultado de PSA con 2 decimales,
 
class Ca_Mama (models.Model):

    OPCIONES_CHOICES=[

        (0,"0 -No aplica"),
        (1,"1 -BIRADS 0: necesidad de nuevo estudio imagenológico o mamograma previo para evaluación"),
        (2,"2 -BIRADS 1: negativo"),
        (3,"3 -BIRADS 2: hallazgos benignos"),
        (4,"4 -BIRADS 3: probablemente benigno"),
        (5,"5 -BIRADS 4: anormalidad sospechosa"),
        (6,"6 -BIRADS 5: altamente sospechoso de malignidad"),
        (7,"7 -BIRADS 6: malignidad por biopsia conocida"),
        (21,"21-Riesgo no evaluado")]
    
    OPCIONES_CHOICES_BIO=[(0 ,"0 -No aplica"),
        (1 ,"1 -Benigna"),
        (2 ,"2 -Atípica (Indeterminada)"),
        (3 ,"3 -Malignidad sospechosa/probable"),
        (4 ,"4 -Maligna"),
        (5 ,"5 -No satisfactoria"),
        (21,"21-Riesgo no evaluado")]

    consecutivo_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    fecha_toma_mamografia = models.DateField()  
    resultado_mamografia =models.SmallIntegerField(choices=OPCIONES_CHOICES)  # -- Resultado de la mamografía
    fecha_toma_biopsia_mama = models.DateField()  # Fecha de toma de biopsia de mama
    fecha_resultado_biopsia_mama = models.DateField()  # Fecha del resultado de la biopsia de mama
    resultado_biopsia_mama =models.SmallIntegerField(choices=OPCIONES_CHOICES_BIO) # Resultado de la biopsia de mama
    
#-- Tabla salud_bucal
class Salud_Bucal (models.Model):
  consecutivo_registro= models.ForeignKey(Registro, on_delete=models.CASCADE)
  fecha_atencion_salud_bucal = models.DateField()  #-- Fecha de atención en salud bucal por profesional en odontología
  cop_por_persona = models.DecimalField(max_digits=12, decimal_places=2) #NOT NULL, -- COP por persona, valor numérico con 2 decimales

#---Tabla para gestacion
class Gestacion (models.Model):

    OPCIONES_CHOICES =[(0,"0 -No aplica"),
    (1,"1 -Sí"),
    (2,"2 -No"),
    (21,"21-Riesgo no evaluado")]

    OPCIONES_CHOICES_A=[(0  ,"0 -No aplica"),
    (1  ,"1 -Sí"),
    (2  ,"2 -No"),
    (21 ,"21-Registro no evaluado")]

    OPCIONES_CHOICES_R=[
    (0,"0 -No aplica"),
    (4,"4 -Alto riesgo"),
    (5,"5 -Bajo riesgo"),
    (21,"21-Riesgo no evaluado")]

    OPCIONES_CHOICES_AF=[(0,"0 -No aplica"),
    (1,"1 -Sí se suministra"),
    (16,"16-No se suministra por una tradición"),
    (17,"17-No se suministra por una condición de salud"),
    (18,"18-No se suministra por negación de la usuaria"),
    (20,"20-No se suministra por otras razones"),
    (21,"21-Registro no evaluado")]
    
    consecutivo_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    gestante =models.SmallIntegerField(choices=OPCIONES_CHOICES)  #NOT NULL, -- 2 dígitos (N)
    acido_folico_preconcepcional =models.SmallIntegerField(choices=OPCIONES_CHOICES_A)  #NOT NULL, -- 2 dígitos (N)
    fecha_probable_parto = models.DateField()  #NOT NULL, -- Fecha probable de parto (F)
    clasificacion_riesgo_gestacional =models.SmallIntegerField(choices=OPCIONES_CHOICES_R) # NOT NULL, -- 2 dígitos (N)
    fecha_atencion_parto = models.DateField()  #NOT NULL, -- Fecha de atención parto o cesárea (F)
    fecha_salida_atencion_parto = models.DateField()  #NOT NULL, -- Fecha de salida de atención parto o cesárea (F)
    fecha_primera_consulta_prenatal = models.DateField() # NOT NULL, -- Fecha de primera consulta prenatal (F)
    fecha_ultimo_control_prenatal = models.DateField()  #NOT NULL, -- Fecha de último control prenatal (F)
    suministro_acido_folico =models.SmallIntegerField(choices=OPCIONES_CHOICES_AF)  #NOT NULL, -- Suministro de ácido fólico en el control prenatal (N)
    suministro_sulfato_ferroso =models.SmallIntegerField(choices=OPCIONES_CHOICES_AF) # NOT NULL, -- Suministro de sulfato ferroso en el control prenatal (N)
    suministro_carbonato_calcio =models.SmallIntegerField(choices=OPCIONES_CHOICES_AF) # NOT NULL, -- Suministro de carbonato de calcio en el control prenatal (N)

class Gestacion_menores_hasta_siente_meses (models.Model):
    consecutivo_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    fecha_atencion_promocion_apoyo_lactancia = models.DateField() 

class No_Reporte (models.Model):

    OPCIONES_CHOICES = [
        (0, 'No aplica'),
        (21, 'Riesgo no evaluado'),
        (1845, 'Registrar'),
   ]
    consecutivo_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    sifilis_gestacional_congenita =models.SmallIntegerField(choices=OPCIONES_CHOICES, default=0)
    hipotiroidismo_congenito =models.SmallIntegerField(choices=OPCIONES_CHOICES, default=0)
    lepra =models.SmallIntegerField(choices=OPCIONES_CHOICES, default=21)
    obesidad_desnutricion =models.SmallIntegerField(choices=OPCIONES_CHOICES, default=21)
    enfermedad_mental =models.SmallIntegerField(choices=OPCIONES_CHOICES, default=21)
    cancer_cervix =models.SmallIntegerField(choices=OPCIONES_CHOICES, default=0)
    dpt_menores =models.SmallIntegerField(choices=OPCIONES_CHOICES, default=0)
    neumococo =models.SmallIntegerField(choices=OPCIONES_CHOICES, default=0) 
    consulta_psicologia = models.DateField(default="1845-01-01") 
    preservativos =models.SmallIntegerField(choices=OPCIONES_CHOICES, default=0) 
    fecha_hemoglobina = models.DateField(default="1845-01-01") 
    tratamiento_sifilis_gestacional =models.SmallIntegerField(choices=OPCIONES_CHOICES, default=0)
    tratamiento_sifilis_congenita =models.SmallIntegerField(choices=OPCIONES_CHOICES, default=0)
  
class Primera_Infancia (models.Model):
      
    OPCIONES_CHOICES = [
        (0, 'No aplica'),
        (1, 'Sí se suministra'),
        (16, 'No se suministra por una tradición'),
        (17, 'No se suministra por una condición de salud'),
        (18, 'No se suministra por negación de la usuaria'),
        (20, 'No se suministra por otras razones'),
        (21, 'Registro no evaluado'),
    ]

    consecutivo_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    Suministro_fortificacion_casera =models.SmallIntegerField(choices=OPCIONES_CHOICES)
    suministro_de_vitamina_A =models.SmallIntegerField(choices=OPCIONES_CHOICES)
    suministro_hierro =models.SmallIntegerField(choices=OPCIONES_CHOICES)
class Recien_Nacidos (models.Model):
  
    OPCIONES_TAM_CHOICES = [
        (0, '0-No aplica'),
        (4, '4-Alterado'),
        (5, '5-Normal'),
        (21, '21-Riesgo no evaluado'),
    ]

    OPCIONES_TAM_AUD_CHOICES = [
        (0, '0-No aplica'),
        (4, '4-No pasó'),
        (5, '5-No pasó'),
        (21, '21-Riesgo no evaluado'),
    ]

    consecutivo_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    resultado_tamizaje_auditivo_neonatal =models.SmallIntegerField(choices=OPCIONES_TAM_AUD_CHOICES) # -- Resultado de tamizaje auditivo neonatal
    resultado_tamizaje_visual_neonatal =models.SmallIntegerField(choices=OPCIONES_TAM_CHOICES)  #  -- Resultado de tamizaje visual neonatal
    resultado_oximetria_pre_post_ductal =models.SmallIntegerField(choices=OPCIONES_TAM_CHOICES) # -- Resultado de tamización con oximetría pre y post ductal
    fecha_oximetria_pre_post_ductal = models.DateField()            # -- Fecha de tamización con oximetría pre y post ductal
    fecha_tamizaje_auditivo_neonatal = models.DateField()           # -- Fecha de tamizaje auditivo neonatal
    fecha_tamizaje_visual_neonatal = models.DateField()             # -- Fecha de tamizaje visual neonatal
    fecha_tsh_neonatal = models.DateField()                     # -- Fecha de TSH neonatal
    resultado_tsh_neonatal =models.SmallIntegerField(choices=OPCIONES_TAM_CHOICES) #               -- Resultado de TSH neonatal
class Riesgo_Cardiovascular (models.Model):
  
    OPCIONES_CHOICES= [(0, "0 -No aplica"),
    (4, "4 -Alto"),
    (5, "5 -Bajo"),
    (6, "6 -Moderado"),
    (21,"21-Riesgo no evaluado")]

    OPCIONES_CHOICES_M=[
    (0, "0 - No aplica"),
    (4, "4 -Alto"),
    (5, "5 -Bajo"),
    (6, "6 -Moderado"),
    (21, "21-Riesgo no evaluado")]

    consecutivo_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    consumo_tabaco =models.SmallIntegerField() #                 -- Consumo de tabaco
    resultado_glicemia_basal =models.SmallIntegerField()   # -- Resultado de glicemia basal
    fecha_toma_ldl = models.DateField() #  
    resultado_ldl = models.BigIntegerField()                 
    resultado_hdl = models.BigIntegerField()   #              -- Resultado de HDL
    resultado_trigliceridos = models.BigIntegerField()   #       -- Resultado de triglicéridos
    fecha_toma_hemoglobina = models.DateField() #                  -- Fecha de toma hemoglobina
    resultado_hemoglobina = models.DecimalField(max_digits=4, decimal_places=2)  #        -- Resultado de hemoglobina
    fecha_toma_glicemia_basal = models.DateField() #             -- Fecha de toma glicemia basal
    fecha_toma_creatinina = models.DateField()  #                   -- Fecha de toma creatinina
    resultado_creatinina = models.DecimalField(max_digits=4, decimal_places=2) #           -- Resultado de creatinina
    fecha_toma_hdl = models.DateField() #                          -- Fecha de toma HDL
    clasificacion_riesgo_cardiovascular =models.SmallIntegerField(choices=OPCIONES_CHOICES) #-- Clasificación del riesgo cardiovascular
    clasificacion_riesgo_metabolico =models.SmallIntegerField(choices=OPCIONES_CHOICES_M) #    -- Clasificación del riesgo metabólico
    fecha_toma_trigliceridos = models.DateField() #                -- Fecha de toma triglicéridos
class Test_0_12 (models.Model):

    OPCIONES_TAM_VALE_CHOICES = [
        (0, '0-No aplica'),
        (4, '4-Falla'),
        (5, '5-Pasa'),
        (21, '21-Riesgo no evaluado'),
    ]
    consecutivo_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    resultado_tamizaje_vale =models.SmallIntegerField(choices=OPCIONES_TAM_VALE_CHOICES)  #    -- Resultado de tamizaje VALE
    fecha_tamizaje_vale = models.DateField() #              -- Fecha de tamizaje VALE   
class Test_0_7 (models.Model):

    OPCIONES_CHOICES = [
    (0, "0 -No aplica"),
    (3, "3 -Sospecha de problemas de desarrollo"),
    (4, "4 -Riesgo de problemas de desarrollo"),
    (5, "5 -Desarrollo esperado para la edad"),
    (21, "21-Riesgo no evaluado")]

    consecutivo_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    resultado_motricidad_gruesa =models.SmallIntegerField(choices=OPCIONES_CHOICES)  #    -- Resultado de escala abreviada de desarrollo área de motricidad gruesa
    resultado_motricidad_finoadaptativa =models.SmallIntegerField(choices=OPCIONES_CHOICES)  #   -- Resultado de escala abreviada de desarrollo área de motricidad finoadaptativa
    resultado_personal_social =models.SmallIntegerField(choices=OPCIONES_CHOICES)  #   -- Resultado de escala abreviada de desarrollo área personal social
    resultado_audicion_lenguaje =models.SmallIntegerField(choices=OPCIONES_CHOICES) # -- Resultado de escala abreviada de desarrollo área de audición y lenguaje

class Test_Mayores_60 (models.Model):

    OPCIONES_CHOICES=[(0, "0 -No aplica"),
    (4, "4 -Sospecha de deterioro cognoscitivo"),
    (5, "5 -Normal"),
    (21, "21-Riesgo no evaluado")]

    consecutivo_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    test_vejez =models.SmallIntegerField(choices=OPCIONES_CHOICES) 
   
class Toda_poblacion (models.Model):

    OPCIONES_CHOICES=[(0, "0 -No aplica"),
    (4, "4 -Reactivo"),
    (5, "5 -No reactivo"),
    (21, "21-Riesgo no evaluado")]

    OPCIONES_CHOICES_S=(0, "0 -No aplica"),
    (4, "4 -Positivo"),
    (5, "5 -Negativo"),
    (21," 21-Riesgo no evaluado")

    consecutivo_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    fecha_peso = models.DateField()              
    peso = models.DecimalField(max_digits=5, decimal_places=2)              
    fecha_talla = models.DateField()     #Fecha de la talla (Toda la población)
    talla =models.SmallIntegerField()               #Talla en centímetros (Toda la población)
    resultado_tamizaje_hepatitis_c =models.SmallIntegerField(choices=OPCIONES_CHOICES)  #-- Resultado de tamizaje para hepatitis C
    fecha_valoracion_integral = models.DateField()    #Fecha de consulta de valoración integral
    fecha_antigeno_hepatitis_b = models.DateField()  # Fecha de antígeno de superficie hepatitis B (Toda la población)
    resultado_antigeno_hepatitis_b =models.SmallIntegerField(choices=OPCIONES_CHOICES) # -- Resultado de antígeno de superficie hepatitis B (Toda la población)
    fecha_tamizaje_sifilis = models.DateField() #     -- Fecha de toma de prueba tamizaje para sífilis
    resultado_tamizaje_sifilis =models.SmallIntegerField( choices=OPCIONES_CHOICES_S) #-- Resultado de prueba tamizaje para sífilis
    fecha_prueba_vih = models.DateField() #        -- Fecha de toma de prueba para VIH
    resultado_prueba_vih =models.SmallIntegerField(choices=OPCIONES_CHOICES_S) #-- Resultado de prueba para VIH
    fecha_tamizaje_hepatitis_c = models.DateField() # -- Fecha de toma de tamizaje hepatitis C
class Tuberculosis (models.Model):

    OPCIONES_CHOICES=[(1 ,"1 -Sí"),
    (2 ,"2 -No"),
    (21,"21-Riesgo no evaluado")]

    OPCIONES_CHOICES_B=[(1, "1 -Negativa"),
    (2, "2 -Positiva"),
    (3, "3 -En proceso"),
    (4, "4 -No"),
    (21, "21-Riesgo no evaluado")]

    consecutivo_registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    Sintomatico_respiratorio =models.SmallIntegerField(choices=OPCIONES_CHOICES) 
    Fecha_baciloscopia  = models.DateField() 
    Resultado_baciloscopia =models.SmallIntegerField(choices=OPCIONES_CHOICES_B) 
    