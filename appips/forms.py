from django import forms
from .models import *
from django import forms

from django import forms


class AgudezaVisualForm(forms.ModelForm):
    class Meta:
        model = AgudezaVisual
        fields = [
            'agudeza_visual_lejana_ojo_izquierdo',
            'agudeza_visual_lejana_ojo_derecho',
            'fecha_valoracion_agudeza_visual',
        ]
        widgets = {
            'fecha_valoracion_agudeza_visual': forms.DateInput(attrs={'type': 'date'}),
        }

class AnticoncepcionForm(forms.ModelForm):
    class Meta:
        model = Anticoncepcion
        fields = ['fecha_atencion_asesoria_anticoncep', 
                  'suministro_metodo_anticoceptivo', 
                  'fecha_sumistro_ant']
        widgets = {
            'fecha_atencion_asesoria_anticoncep': forms.DateInput(attrs={'type': 'date'}),
            'fecha_sumistro_ant': forms.DateInput(attrs={'type': 'date'}),
        }

class CaCervixForm(forms.ModelForm):
    class Meta:
        model = Ca_Cervix
        fields = [
                    'tratamiento_ablativo_escision',
                    'tamizaje_cancer_cuello_uterino',
                    'fecha_tamizaje_cancer_cuello_uterino',
                    'resultado_tamizaje_cancer_cuello_uterino',
                    'calidad_muestra_citologia',
                    'codigo_habilitacion_ips_cancer_cuello_uterino',
                    'fecha_colposcopia',
                    'fecha_biopsia_cervicouterina',
                    'resultado_biopsia_cervicouterina']
        widgets = {
            'fecha_tamizaje_cancer_cuello_uterino': forms.DateInput(attrs={'type': 'date'}),
            'fecha_colposcopia': forms.DateInput(attrs={'type': 'date'}),
            'fecha_biopsia_cervicouterina': forms.DateInput(attrs={'type': 'date'})
        }
        

class CaColonForm(forms.ModelForm):

    class Meta:
        model = Ca_Colon
        fields = [
                'resultado_prueba_sangre_oculta_mf' ,
                'resultado_colonoscopia_tamizaje', 
                'fecha_colonoscopia_tamizaje' ,  
                'fecha_prueba_sangre_oculta']
        widgets = {
            'fecha_colonoscopia_tamizaje': forms.DateInput(attrs={'type': 'date'}),
            'fecha_prueba_sangre_oculta': forms.DateInput(attrs={'type': 'date'})
        }

class CaProstataForm(forms.ModelForm):

    class Meta:
        model = Ca_Prostata
        fields = [ 'resultado_tacto_rectal', 'fecha_tacto_rectal','fecha_toma_psa','resultado_psa' ]
        widgets = {
            'fecha_tacto_rectal': forms.DateInput(attrs={'type': 'date'}),
            'fecha_toma_psa': forms.DateInput(attrs={'type': 'date'})
        }

class CaMamaForm(forms.ModelForm):

    class Meta:
        model = Ca_Mama
        fields = [  'fecha_toma_mamografia','resultado_mamografia', 'fecha_toma_biopsia_mama', 'fecha_resultado_biopsia_mama', 'resultado_biopsia_mama']
        widgets = {
            'fecha_toma_mamografia': forms.DateInput(attrs={'type': 'date'}),
            'resultado_mamografia': forms.DateInput(attrs={'type': 'date'}),
            'fecha_resultado_biopsia_mama': forms.DateInput(attrs={'type': 'date'})
        }

class SaludBucalForm(forms.ModelForm):
    class Meta:
        model = Salud_Bucal
        fields = [ 'fecha_atencion_salud_bucal',
          'cop_por_persona' ]
        widgets = {
           'fecha_atencion_salud_bucal' : forms.DateInput(attrs={'type': 'date'}),
        }

class GestacionForm(forms.ModelForm):
    class Meta:
        model = Gestacion
        fields = '__all__'
        exclude = ['consecutivo_registro']
        widgets = {
           'fecha_probable_parto' : forms.DateInput(attrs={'type': 'date'}),
           'fecha_atencion_parto':forms.DateInput(attrs={'type': 'date'}),
           'fecha_salida_atencion_parto':forms.DateInput(attrs={'type': 'date'}),
           'fecha_primera_consulta_prenatal':forms.DateInput(attrs={'type': 'date'}),
           'fecha_ultimo_control_prenatal':forms.DateInput(attrs={'type': 'date'}),
        }

class GestacionmenoresForm(forms.ModelForm):
    class Meta:
        model=Gestacion_menores_hasta_siente_meses
        fields = '__all__'
        exclude = ['consecutivo_registro']
        widgets ={ 'fecha_atencion_promocion_apoyo_lactancia':forms.DateInput(attrs={'type': 'date'})}

class NoReporteForm(forms.ModelForm):
    class Meta:
        model=No_Reporte
        fields = '__all__'
        exclude = ['consecutivo_registro']
        widgets ={ 'consulta_psicologia':forms.DateInput(attrs={'type': 'date'}),'fecha_hemoglobina':forms.DateInput(attrs={'type': 'date'})}


class PrimeraInfanciaForm(forms.ModelForm):
    class Meta:
        model=Primera_Infancia
        fields = '__all__'
        exclude = ['consecutivo_registro']



class RecienNacidoForm(forms.ModelForm):
    class Meta:
        model=Recien_Nacidos
        fields = '__all__'
        exclude = ['consecutivo_registro']
        widgets ={ 'fecha_oximetria_pre_post_ductal':forms.DateInput(attrs={'type': 'date'}),'fecha_hemoglobina':forms.DateInput(attrs={'type': 'date'}),
            'fecha_tamizaje_auditivo_neonatal':forms.DateInput(attrs={'type': 'date'}),'fecha_hemoglobina':forms.DateInput(attrs={'type': 'date'}),
            'fecha_tamizaje_visual_neonatal':forms.DateInput(attrs={'type': 'date'}),'fecha_hemoglobina':forms.DateInput(attrs={'type': 'date'}),
            'fecha_tsh_neonatal':forms.DateInput(attrs={'type': 'date'}),'fecha_hemoglobina':forms.DateInput(attrs={'type': 'date'})        
        }

class RiesgoCardiovascularForm(forms.ModelForm):
    class Meta:
        model=Riesgo_Cardiovascular
        fields = '__all__'
        exclude = ['consecutivo_registro']
        widgets = {
           'fecha_toma_ldl' : forms.DateInput(attrs={'type': 'date'}),
           'fecha_toma_hemoglobina':forms.DateInput(attrs={'type': 'date'}),
           'fecha_toma_glicemia_basal':forms.DateInput(attrs={'type': 'date'}),
           'fecha_toma_creatinina':forms.DateInput(attrs={'type': 'date'}),
           'fecha_toma_hdl':forms.DateInput(attrs={'type': 'date'}),
           'fecha_toma_trigliceridos':forms.DateInput(attrs={'type': 'date'})
        }

class  Test_0_12Form(forms.ModelForm):
    class Meta:
        model=Test_0_12
        fields = '__all__'
        exclude = ['consecutivo_registro']
        widgets = {
           'fecha_tamizaje_vale' : forms.DateInput(attrs={'type': 'date'}),
        }

class  Test_0_7Form(forms.ModelForm):
    class Meta:
        model=Test_0_7
        fields = '__all__'
        exclude = ['consecutivo_registro']


   

class  Test_Mayores_60Form(forms.ModelForm):
    class Meta:
        model= Test_Mayores_60
        fields = '__all__'
        exclude = ['consecutivo_registro']

        #Toda_poblacion

class  Toda_poblacionForm(forms.ModelForm):
    class Meta:
        model= Toda_poblacion
        fields = '__all__'
        exclude = ['consecutivo_registro']
        widgets = {
           'fecha_peso fecha_talla' : forms.DateInput(attrs={'type': 'date'}),
           'fecha_valoracion_integral' : forms.DateInput(attrs={'type': 'date'}),
           'fecha_antigeno_hepatitis_b' : forms.DateInput(attrs={'type': 'date'}),
           'fecha_tamizaje_sifilis' : forms.DateInput(attrs={'type': 'date'}),
           'fecha_prueba_vih' : forms.DateInput(attrs={'type': 'date'}),
           'fecha_tamizaje_hepatitis_c' : forms.DateInput(attrs={'type': 'date'}),
        }

#Tuberculosis     
class  TuberculosisForm(forms.ModelForm):
    class Meta:
        model= Tuberculosis
        fields = '__all__'
        exclude = ['consecutivo_registro']
        widgets = {
           'Fecha_baciloscopia' : forms.DateInput(attrs={'type': 'date'}),

        } 
