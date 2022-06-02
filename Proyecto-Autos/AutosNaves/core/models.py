from django.db import models

# Create your models here.

class Tipo(models.Model):
    idTipo = models.IntegerField(primary_key=True, verbose_name='Id del tipo')
    nombreTipo = models.CharField(max_length=20, verbose_name='Nombre del tipo', blank=False, null=False)

    def __str__(self):
        return self.nombreTipo


class Auto(models.Model):
    idAuto =models.IntegerField(primary_key=True, verbose_name='Id auto')
    nombreA =models.CharField(max_length=40, verbose_name=' Nombre auto')
    img1 =models.ImageField(upload_to='imagen especificacion')
    texto1 =models.CharField(max_length=40, verbose_name=' especificaciones1')
    img2 =models.ImageField(upload_to='imagen especificacion')
    texto2 =models.CharField(max_length=40, verbose_name=' especificaciones2')
    img3 =models.ImageField(upload_to='imagen especificacion')
    texto3 =models.CharField(max_length=40, verbose_name=' especificaciones3')
    img4 =models.ImageField(upload_to='imagen especificacion')
    texto4 =models.CharField(max_length=40, verbose_name=' especificaciones4')
    precio =models.IntegerField(verbose_name='Precio auto')
    Galeria1 =models.ImageField(upload_to='Galeria1')
    Galeria2 =models.ImageField(upload_to='Galeria2')
    Galeria3 =models.ImageField(upload_to='Galeria3')
    Galeria4 =models.ImageField(upload_to='Galeria4')
    Galeria5 =models.ImageField(upload_to='Galeria5')
    Galeria6 =models.ImageField(upload_to='Galeria6')
    datoA =models.TextField(verbose_name='Descripcion auto 1')
    datoB =models.TextField(verbose_name='Descripcion auto 2')
    videoUrl =models.CharField(max_length=280, verbose_name='Url video')
    idtipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)



    def str(self):
        return self.nombreA