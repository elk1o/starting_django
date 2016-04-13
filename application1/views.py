#-*- coding: utf-8 -*-
from django.shortcuts import render               #Renderización genérica
from django.http import HttpResponse              #Importar plantilla de respuestas automáticas de las páginas con protocolo http
from django.shortcuts import render_to_response   #Renderización de la respuesta
from django.conf import settings                  #Importar configuracion del fichero settings.py
from django.http import HttpResponseRedirect      #Importar respuestas directas al protocolo http (Páginas al vuelo: Ej: cad = "<html>[...]<h1>hola!</h1>[...]</html>")
from django.template import RequestContext        #Comunicación M+C con V
from application1.models import Categoria, Espectaculo, Lugar

# Create your views here.
def index(request):
    categories = Categoria.objects.all()
    return render_to_response('index.html', {'categories': categories})

def detalle(request, categoria_id):
    return HttpResponse('detalle %s' % categoria_id)

def categorias(request, categoria_id):
    show = Espectaculo.objects.filter(id=categoria_id)
    return render_to_response('espectaculos.html',{'show':show})