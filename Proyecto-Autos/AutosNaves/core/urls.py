from django.contrib import admin
from django.urls import path
from .views import home, CHEVROLET, FORD, HYUNDAI, JEEP

urlpatterns = [
    path('', home,name="home"),
    path('CHEVROLET/',CHEVROLET,name="CHEVROLET"),
    path('FORD/',FORD,name="FORD"),
    path('HYUNDAI/',HYUNDAI,name="HYUNDAI"),
    path('JEEP/',JEEP,name="JEEP"),
]