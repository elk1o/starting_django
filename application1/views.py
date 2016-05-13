#-*- coding: utf-8 -*-
from django.shortcuts import render               #Renderización genérica
from django.http import HttpResponse, Http404     #Importar plantilla de respuestas automáticas de las páginas con protocolo http
from django.shortcuts import render_to_response   #Renderización de la respuesta
from django.conf import settings              #Importar configuracion del fichero settings.py
from django.http import HttpResponseRedirect      #Importar respuestas directas al protocolo http (Páginas al vuelo: Ej: cad = "<html>[...]<h1>hola!</h1>[...]</html>")
from django.template import RequestContext        #Comunicación M+C con V
from application1.models import Categoria, Espectaculo, Lugar
from application1.forms import Formulario1
from django.core.mail import send_mail, EmailMessage   #pertenecen al módulo smtplib(Django library)
import sys
import datetime


# Create your views here.
def index(request):
    categories = Categoria.objects.all()
    return render_to_response('index.html', {'categories': categories})

def detalle(request, categoria_id):
    return HttpResponse('detalle %s' % categoria_id)

def categorias(request, categoria_id):
    print(settings.BASE_DIR)
    print(sys.path)
    show = Espectaculo.objects.filter(id=categoria_id)
    return render_to_response('espectaculos.html',{'show':show})

def espectaculos(request, espectaculo_id):
    print(settings.BASE_DIR)
    espectaculos = Espectaculo.objects.all()
    return render_to_response('detalle_evento.html',{'espectaculos':espectaculos})

def ayuda(request):
    mensaje=" Bienvenidos"
    ctx= {'msg':mensaje}
    return render_to_response('index.html', context_instance= RequestContext(request))


def informa(request):
    hora= datetime.datetime.now()
    html ="<html><body><h2>Fecha: %s </h2></body></html>" % hora
    return HttpResponse(html)

def hola(request):
    return HttpResponse("Bienvenidos")

def horas_adelante(request, horas):
    try:
        horas = int(horas)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=horas)
    html = "<html><body><h2>En %s hora(s), serán las %s </h2></body></html>" % (horas, dt)
    return HttpResponse(html)


def info_navegador(request):
    try:
        info = request.META['REMOTE_ADDR']
        # info = request.META['HTTP_REFERER']
        # info = request.META['HTTP_USER_AGENT']
    except KeyError:
        info = "Desconocido"
    return HttpResponse("El navegador es %s" % info)

def info_navegador1(request):
    try:
        info = request.META.items()
        # info.sort()
        html = []
        for k, v in info:
            html.append("<tr><td>%s</td><td>%s</td></tr>" % (k,v))
    except KeyError:
        info = "Desconocido"
    return HttpResponse("<table border=1>%s</table>" % "\n".join(html))

# formularios implícitos en plantilla -----------------------------------------------------------
def formulario_busqueda(request):
    return render(request, "formulario1.html")

def formulario_busqueda1(request):
    if "q" in request.GET and request.GET['q']:
        q = request.GET['q']
        categorias = Categoria.objects.filter(categoria=q)
        return render(request, "gracias.html", {"categorias":categorias, "query":q })
    else:
        #return HttpResponse("Por favor, introduzca los datos correctamente.")
        return render(request,"gracias.html", {"error": True})


def formulario_busqueda2(request):
    error = False
    if "q" in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) >20:
            error = True
        else:
            categorias = Categoria.objects.filter(categoria=q)
            return render(request, "gracias.html", {"categorias":categorias, "query":q })
    return render(request,"gracias.html", {"error": error})

# formularios explícitos (Clase-Plantilla)--------------------------------------------------------
def formulario1(request):
     if request.method == 'POST':
        formu = Formulario1(request.POST)
        print(str(formu))
        if formu.is_valid():
            return HttpResponseRedirect('/gracias1')
        else:
             formu = Formulario1()
        return render(request, 'formulario_backend.html', {'formu': formu} )

     formu = Formulario1()
     return render(request, 'formulario_backend.html', {'formu': formu})

def gracias(request):
    msg = "<html><head></head><body>Gracias :) </body></html>"
    return HttpResponse(msg)

def contactos(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('nombre', ''):
            errors.append('Campo nombre vacío')

        if not request.POST.get('mensaje', ''):
            errors.append('Campo mensaje vacío')

        if not request.POST.get('email', '') and '@' not in request.POST['email']:
            errors.append('Dirección inválida de email')

        if not errors:
            send_mail(request.POST['nombre'],request.POST['mensaje'], 'e.flores@gobalo.es', [request.POST['email']],)
            #envia= EmailMessage()
            #envia.send()
            return gracias(request)
        print(errors)
        formu = Formulario1()
        return render(request, 'formulario_backend.html', {'errors': errors, 'formu':formu})
    else:
        formu=Formulario1()
        return render(request, 'formulario_backend.html', {'errors': errors, 'formu':formu})


def contactos_datoslimpios(request):
    if request.method == 'POST':
        formu = Formulario1(request.POST)
        if formu.is_valid():
            cd= formu.cleaned_data
            send_mail(
                cd['nombre'],
                cd['mensaje'],
                'test@test.com',
                ['e.flores@gobalo.es'],
                # cd.get('email', 'e.flores@gobalo.es'),  # En vez de coger del formulario, asigna valor al campo
            )
            return HttpResponseRedirect('/gracias1/')
        else:
            # print(formu.errors)
            return render(request, 'formulario_backend.html', {'formu': formu, 'errors': formu.errors})
            # formu = Formulario1(initial={'nombre':'asunto por defecto'})
            # return render(request,'formulario_backend.html',{formu:'formu'})
    else:
        formu= Formulario1()
        # formu = Formulario1(initial={'nombre': 'asunto por defecto'})
        return render(request, 'formulario_backend.html', {'formu':formu})
