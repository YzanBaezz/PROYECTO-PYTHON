from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'core/pagina-home.html')

#---------------------INICIO/REGISTRO-----------------

def inicioSesion(request):

    return render(request, 'core/inicio-sesion.html')

def RegistroSesion(request):

    return render(request, 'core/registro-sesion.html')

#-----------------------MARCAS-------------------------

def Marcas(request):

    return render(request, 'core/Marcas.html')

def CHEVROLET(request):

    return render(request, 'core/CHEVROLET.html')

def FORD(request):

    return render(request, 'core/FORD.html')

def HYUNDAI(request):

    return render(request, 'core/HYUNDAI.html')

def JEEP(request):

    return render(request, 'core/JEEP.html')

#-----------------------PLANTILLAS------------------------

def marcas(request):
    contexto = {"nombreM":"Manchas2", "edadM":"2 años","colorP":"Castaño","imagenM":"/static/core/img/pet1.jpeg"}
    return render(request,'core/mascota.html',contexto)


#-------------------------mapa-api------------------------

def mapa(request):

    return render(request, 'core/mapa.html')


#----------------------AUTOS Y CAMIONETAS ---------------

#--Chevrolet--

def camaro(request):

    return render(request, 'core/ChevroletCamaro.html')


def onix(request):

    return render(request, 'core/ChevroletOnixSedan.html')

def sail(request):

    return render(request, 'core/ChevroletSail.html')

#--Ford--

def territory(request):

    return render(request, 'core/FordAllNewTerritory.html')

def focus(request):

    return render(request, 'core/FordFocus.html')

def raptor(request):

    return render(request, 'core/FordRaptor.html')

#--Hyundai--

def accent(request):

    return render(request, 'core/HyundaiAccent.html')

def tucson(request):

    return render(request, 'core/HyundaiTucson.html')

def veloster(request):

    return render(request, 'core/HyundaiVeloster.html')

#--Jeep--

def cherokee(request):

    return render(request, 'core/JeepCherokee.html')

def gladiator(request):

    return render(request, 'core/JeepGladiator.html')

def wrangler(request):

    return render(request, 'core/JeepWrangler.html')