from django.contrib import admin
from django.urls import path
from .views import home, CHEVROLET, FORD, HYUNDAI, JEEP, mapa, Marcas, camaro, territory

urlpatterns = [
    path('', home,name="home"),
    path('CHEVROLET/', CHEVROLET,name="CHEVROLET"),
    path('FORD/', FORD,name="FORD"),
    path('HYUNDAI/', HYUNDAI,name="HYUNDAI"),
    path('JEEP/', JEEP,name="JEEP"),
    path('mapa/', mapa,name="mapa"),
    path('Marcas/', Marcas,name="Marcas"),
    path('ChevroletCamaro/', camaro, name="camaro"),
    

    path('FordAllNewTerritory/', territory, name="territory")

]