from django.http import HttpResponse
from django.shortcuts import render
from .models import Directores, Peliculas
from django.views import generic


# Create your views here.
class director(object):

   def __int__(self,nombre,apellido,fecha_nacimiento):
      self.nombre=nombre
      self.apellido=apellido
      self.fecha_nacimiento=fecha_nacimiento


def directores(request):

   dir=Directores.objects.all()

   return render(request, "directores.html",{'datosdirector':dir})

def direct(request,nombre_director):

   separar=nombre_director.split('_')
   nombre=separar[0]
   apellido=separar[1]
   datos_director=Directores.objects.get(nombre=nombre,apellido=apellido)
   pelis = Peliculas.objects.all()
   return render(request, "director.html",{'datos':datos_director,'peli':pelis})

def infopelicula(request,pelicula):

   info=Peliculas.objects.get(nombre=pelicula)
   dir=str(info.director)
   urlDirector= dir.replace(" ","_")
   return render(request,"peliculas.html",{'infopeli':info,'urlDirector':urlDirector})


