from django.contrib import admin
from django.urls import path
from .views import home, CHEVROLET, FORD, HYUNDAI, JEEP, mapa, Marcas, camaro, onix, sail, territory, focus, raptor, accent, tucson, veloster, cherokee, gladiator, wrangler, admin, AgregarAutos, Autos, Camionetas,InicioSesion, RegistroSesion, PerfilUsuario, AtencionCliente, EditarPerfil, AutosNuevos, AutosSemiNuevos


urlpatterns = [
    path('', home,name="home"),
    path('CHEVROLET/', CHEVROLET,name="CHEVROLET"),
    path('FORD/', FORD,name="FORD"),
    path('HYUNDAI/', HYUNDAI,name="HYUNDAI"),
    path('JEEP/', JEEP,name="JEEP"),
    path('mapa/', mapa,name="mapa"),
    path('Marcas/', Marcas,name="Marcas"),
    path('ChevroletCamaro/', camaro, name="camaro"),
    path('ChevroletOnixSedan/',onix, name="onix"),
    path('ChevroletSail/', sail, name="sail"),
    path('FordAllNewTerritory/', territory, name="territory"),
    path('FordFocus/', focus, name="focus"),
    path('FordRaptor/', raptor, name="raptor"),
    path('HyundaiAccent/', accent, name="accent"),
    path('HyundaiTucson/', tucson, name="tucson"),
    path('HyundaiVeloster/', veloster, name="veloster"),
    path('JeepCherokee/', cherokee, name="cherokee"),
    path('JeepGladiator/', gladiator, name="gladiator"),
    path('JeepWrangler/', wrangler, name="wrangler"),
    path('admin/', admin, name="administrador"),
    path('AgregarAutos/', AgregarAutos, name="AgregarAutos"),
    path('Autos/', Autos, name="Autos"),
    path('Camionetas/', Camionetas, name="Camionetas"),
    path('InicioSesion/' ,InicioSesion, name="InicioSesion"),
    path('RegistroSesion/',RegistroSesion, name="RegistroSesion"),
    path('PerfilUsuario/', PerfilUsuario, name="PerfilUsuario"),
    path('AtencionCliente/', AtencionCliente, name="AtencionCliente"),
    path('EditarPerfil/', EditarPerfil, name="EditarPerfil"),
    path('AutosNuevos/', AutosNuevos, name="AutosNuevos"),
    path('AutosSemiNuevos/', AutosSemiNuevos, name="AutosSemiNuevos"),


]