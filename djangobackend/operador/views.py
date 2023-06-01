from django.shortcuts import render
from .models import Trabajador, Area, Departamento,Cargo, Perfiles
from .forms import TrabajadorForm, areaForm, cargoForm, dptoForm, perfilForm

# Create your views here.
# views.py
def login(request):
    return render(request, 'login.html')

def inicio(request):
    return render(request, 'base.html')

# Vistas Trabajadores
def lista_trabajadores(request):
    trabajadores = Trabajador.objects.all()
    context = {
        'trabajadores': trabajadores
    }
    return render(request, 'trabajador/lista_trabajadores.html', context)

def agregar_trabajador(request):
    form = TrabajadorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TrabajadorForm()

    context = {
        'form': form
    }
    return render(request, 'trabajador/agregar_trabajador.html', context)


# Vistas Areas
def lista_areas(request):
    areas = Area.objects.all()
    context = {
        'areas': areas
    }
    return render(request, 'areas/lista_areas.html', context)

def agregar_areas(request):
    formareas = areaForm(request.POST or None)
    if formareas.is_valid():
        formareas.save()
        formareas = areaForm()

    context = {
        'form': formareas
    }
    return render(request, 'areas/agregar_area.html', context)

# Vistas Departamentos
def lista_dptos(request):
    departamentos = Departamento.objects.all()
    context = {
        'departamentos': departamentos
    }
    return render(request, 'departamentos/lista_dptos.html', context)

def agregar_dpto(request):
    formdpto = dptoForm(request.POST or None)
    if formdpto.is_valid():
        formdpto.save()
        formdpto = dptoForm()

    context = {
        'form': formdpto
    }
    return render(request, 'departamentos/agregar_dpto.html', context)

# Vista Cargos
def lista_cargos(request):
    cargos = Cargo.objects.all()
    context = {
        'cargos': cargos
    }
    return render(request, 'cargos/lista_cargos.html', context)

def agregar_cargo(request):
    formcargo = cargoForm(request.POST or None)
    if formcargo.is_valid():
        formcargo.save()
        formcargo = cargoForm()

    context = {
        'form': formcargo
    }
    return render(request, 'cargos/agregar_cargo.html', context)

# Vista Perfiles
def lista_perfiles(request):
    perfiles = Perfiles.objects.all()
    context = {
        'perfiles': perfiles
    }
    return render(request, 'perfiles_usuarios/lista_perfiles.html', context)

def agregar_perfil(request):
    formperfil = perfilForm(request.POST or None)
    if formperfil.is_valid():
        formperfil.save()
        formperfil = perfilForm()

    context = {
        'form': formperfil
    }
    return render(request, 'perfiles_usuarios/agregar_perfil.html', context)