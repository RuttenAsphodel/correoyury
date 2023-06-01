# Importa los formularios de Django
from django import forms

# Importa el modelo Trabajador
from .models import Trabajador, Area, Departamento, Cargo, Perfiles

# Crea el formulario para Trabajador
class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = [
            'id_trabajador',
            'rut_trabajador',
            'nombre_trabajador',
            'sexo',
            'direccion_trabajador',
            'fecha_ingreso',
            'id_area',
            'id_departamento',
            'id_cargo',
            'id_contacto',
            'id_cargas_familiares',
        ]

# Formulario para Areas    
class areaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = '__all__'
        
# Formulario para Departamentos
class dptoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'
        
# Formulario para Cargos
class cargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'
        
# Formulario para perfiles
class perfilForm(forms.ModelForm):
    class Meta:
        model = Perfiles
        fields = '__all__'
        