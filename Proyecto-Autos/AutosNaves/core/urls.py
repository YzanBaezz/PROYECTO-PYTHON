from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import home, CHEVROLET, FORD, HYUNDAI, JEEP, mapa, Marcas, admin, AgregarAutos, Autos, Camionetas,InicioSesion, RegistroSesion, PerfilUsuario, AtencionCliente, EditarPerfil, Catalogo, Auto, registro
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home,name="home"),
    path('CHEVROLET/', CHEVROLET,name="CHEVROLET"),
    path('FORD/', FORD,name="FORD"),
    path('HYUNDAI/', HYUNDAI,name="HYUNDAI"),
    path('JEEP/', JEEP,name="JEEP"),
    path('mapa/', mapa,name="mapa"),
    path('Marcas/', Marcas,name="Marcas"),
    path('Auto/', Auto, name="Auto"),
    path('Administrador/', admin, name="administrador"),
    path('AgregarAutos/', AgregarAutos, name="AgregarAutos"),
    path('Autos/', Autos, name="Autos"),
    path('Camionetas/', Camionetas, name="Camionetas"),
    path('InicioSesion/' ,InicioSesion, name="InicioSesion"),
    path('RegistroSesion/',RegistroSesion, name="RegistroSesion"),
    path('PerfilUsuario/', PerfilUsuario, name="PerfilUsuario"),
    path('AtencionCliente/', AtencionCliente, name="AtencionCliente"),
    path('EditarPerfil/', EditarPerfil, name="EditarPerfil"),
    path('Catalogo/', Catalogo, name= "Catalogo"),

    path('login/', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name="logout"),
    path('registro/', registro, name="registro"),
]