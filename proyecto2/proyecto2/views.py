from django.http import HttpResponse
from django.template import Template, Context

import datetime, random
from miapp.models import *

def bienvenido1(request):
    return HttpResponse("Bienvenidos a la comision 50200, hace horas que estoy probando esto...")

def bienvenido2(request, nombre):
    respuesta = f"Bienvenido {nombre} a la comision 50200"
    return HttpResponse(respuesta)

def bienvenido3(request):
    hoy = datetime.datetime.now()
    respuesta = f"""
    <body>
        <html>
        <h1>Bienvenido al curso de Django!!</h1>
        <h2>Esta es la comision 50200</h2>
        <h3>Hoy es {hoy} </h3>
    <body>
    </html>
    """
    return HttpResponse(respuesta)

def bienvenido_template(request):
    hoy = datetime.datetime.now()
    miHtml = open ("C:/Users/Usuario/Desktop/50200/proyecto2/proyecto2/plantillas/bienvenido.html")
    nombre = "Amadeus"
    apellido = "Mozart"
    diccionario = {"nombre": nombre, "apellido": apellido, 
                   "author": "Daniel Medina", "hoy": hoy}
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context(diccionario)
    respuesta = plantilla.render(miContexto)
    return HttpResponse(respuesta)

def nuevo_curso(request):
    nro_comision = random.randint(1,99999)
    str_nombre = "Python " + str(nro_comision)
    curso = Curso(nombre=str_nombre, comision=nro_comision)
    curso.save()
    documento = f"<html><h1>Se guardo {str_nombre} y comison {nro_comision}<h1><html>"
    return HttpResponse(documento)