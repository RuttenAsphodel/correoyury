# Importa los modelos de Django
from django.db import models

# Crea el modelo Trabajador
class Trabajador(models.Model):
    id_trabajador = models.AutoField(primary_key=True)
    rut_trabajador = models.CharField(max_length=50)
    nombre_trabajador = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    direccion_trabajador = models.CharField(max_length=200)
    fecha_ingreso = models.DateField()
    id_area = models.ForeignKey('Area', on_delete=models.CASCADE)
    id_departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE)
    id_cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE)
    id_contacto = models.CharField(max_length=100)
    id_cargas_familiares = models.IntegerField()

    # Define la representación de cad de instancia de Trabajador
    def __str__(self):
        return self.nombre_trabajador

# Crea los modelos restantes si no los tienes creados
class Area(models.Model):
    nombre_area = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_area

class Departamento(models.Model):
    nombre_departamento = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_departamento

class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_cargo
    
class Perfiles(models.Model):
    rut_trabajador = models.CharField(max_length=50, default="12345678-9")
    cargo =  models.ForeignKey(Cargo, on_delete=models.CASCADE)
    password =  models.CharField(max_length=12, default="6-qL8@_gzaG+ed+4")
    
    def __str__(self):
        return self.rut_trabajador