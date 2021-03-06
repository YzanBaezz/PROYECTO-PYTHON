from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.

def home(request):

    return render(request, 'core/pagina-home.html')

def login(request):

    return render(request, 'core/login.html')

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('PerfilUsuario')
    else:
        form = UserRegisterForm()
    
    contexto = { 'form' : form }
    return render(request, 'core/registro.html', contexto)

def logout(request):

    return render(request, 'core/logout.html')
#---------------------INICIO/REGISTRO/PerfilUsuario-----------------

def InicioSesion(request):

    return render(request, 'core/InicioSesion.html')

def RegistroSesion(request):

    return render(request, 'core/RegistroSesion.html')

def PerfilUsuario(request):

    return render(request, 'core/PerfilUsuario.html')

def Catalogo(request):
    return render(request, 'core/Catalogo.html' )

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

def Auto(request):
    contexto = {"nombreA":"Camaro", "img":"/static/core/img/ChevroletCamaro/Baner-camaro.jpg"
                ,"img1":"/static/core/img/ChevroletCamaro/motor-camaro.png","texto1":"6.2"
                ,"img2":"/static/core/img/ChevroletCamaro/caja-camaro.png","texto2":"CAJA AUTO"
                ,"img3":"/static/core/img/ChevroletCamaro/velocimetro-camaro.png","texto3":"0 A 100 KM/H"
                ,"img4":"/static/core/img/ChevroletCamaro/certificacion-camaro.png","texto4":"Servicio"
                ,"galeriaimg1":"/static/core/img/ChevroletCamaro/galeria1.jpg"
                ,"galeriaimg2":"/static/core/img/ChevroletCamaro/galeria2.jpg"
                ,"galeriaimg3":"/static/core/img/ChevroletCamaro/galeria3.jpg"
                ,"galeriaimg4":"/static/core/img/ChevroletCamaro/galeria4.jpg"
                ,"galeriaimg5":"/static/core/img/ChevroletCamaro/galeria5.jpg"
                ,"galeriaimg6":"/static/core/img/ChevroletCamaro/galeria6.jpg"
                ,"nombreG":"Galeria de Imagenes"
                ,"datosA":"Un facelift al performance." 
                ,"datosB":"El nuevo Camaro fue redise??ado de principio a fin. Su l??nea ha evolucionado para verse a??n mas estilizada, pero eso no es todo, incluye tecnolog??a, performance y un manejo superior. Acel??ralo hasta el fondo y descubre lo que significa la adrenalina."
                ,"videoA":"https://www.youtube.com/embed/0ZzMcwdb2W0"}
    return render(request,'core/Auto.html',contexto)

def Au(request, id):
    a = Auto.objects.get(idAuto = id)
    contexto = {"x": a}
    return render(request, 'core/Auto.html',contexto)

# Administrador

def admin(request):
    return render(request, 'core/Administrador.html')

#-------------------------mapa-api------------------------

def mapa(request):

    return render(request, 'core/mapa.html')


#----------------------AUTOS Y CAMIONETAS ---------------


# Agregar Autos

def AgregarAutos(request):
    return render(request, 'core/AgregarAutos.html')

# Seccion Autos

def Autos(request):
    return render(request, 'core/Autos.html')

# Seccion Camionetas

def Camionetas(request):
    return render(request, 'core/Camionetas.html')

def AtencionCliente(request):
    return render(request, 'core/AtencionCliente.html')

def EditarPerfil(request):
    return render(request, 'core/EditarPerfil.html')
