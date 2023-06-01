from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('inicio', views.inicio, name='inicio'),
    
    path('trabajador/lista_trabajadores', views.lista_trabajadores, name='lista_trabajadores'),
    path('trabajador/agregar_trabajador', views.agregar_trabajador, name='agregar_trabajador'),
    
    path('areas/lista_areas', views.lista_areas, name='lista_areas'),
    path('areas/agregar_area', views.agregar_areas, name='agregar_area'),
    
    path('departamentos/lista_dptos', views.lista_dptos, name='lista_dptos'),
    path('departamentos/agregar_dpto', views.agregar_dpto, name='agregar_dpto'),
    
    path('cargos/lista_cargos', views.lista_cargos, name='lista_cargos'),
    path('cargos/agregar_cargo', views.agregar_cargo, name='agregar_cargo'),
    
    path('perfiles_usuarios/lista_perfiles', views.lista_perfiles, name='lista_perfiles'),
    path('perfiles_usuarios/agregar_perfil', views.agregar_perfil, name='agregar_perfil'),
    
]
