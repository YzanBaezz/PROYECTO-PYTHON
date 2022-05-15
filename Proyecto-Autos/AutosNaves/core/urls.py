from django.contrib import admin
from django.urls import path
from .views import home, CHEVROLET, FORD, HYUNDAI, JEEP, mapa, Marcas, camaro, territory, admin, AgregarAutos, Autos, Camionetas,InicioSesion, RegistroSesion, PerfilUsuario, AtencionCliente, EditarPerfil


urlpatterns = [
    path('', home,name="home"),
    path('CHEVROLET/', CHEVROLET,name="CHEVROLET"),
    path('FORD/', FORD,name="FORD"),
    path('HYUNDAI/', HYUNDAI,name="HYUNDAI"),
    path('JEEP/', JEEP,name="JEEP"),
    path('mapa/', mapa,name="mapa"),
    path('Marcas/', Marcas,name="Marcas"),
    path('ChevroletCamaro/', camaro, name="camaro"),
    

    path('FordAllNewTerritory/', territory, name="territory"),

    path('admin/', admin, name="administrador"),
    path('AgregarAutos/', AgregarAutos, name="AgregarAutos"),
    path('Autos/', Autos, name="Autos"),
    path('Camionetas/', Camionetas, name="Camionetas"),
    path('InicioSesion/' ,InicioSesion, name="InicioSesion"),
    path('RegistroSesion/',RegistroSesion, name="RegistroSesion"),
    path('PerfilUsuario/', PerfilUsuario, name="PerfilUsuario"),
    path('AtencionCliente/', AtencionCliente, name="AtencionCliente"),
    path('EditarPerfil/', EditarPerfil, name="EditarPerfil"),


]