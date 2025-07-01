from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Auto


def inicio(request):
    # return HttpResponse("<h1>Estoy en el inicio</h1>")
    return render(request, 'index.html')


def saludo(request,nombre,apellido):
    fecha = datetime.now()
    return HttpResponse(f"<h1>{fecha.strftime('%H:%M:%S')} Hola {nombre} {apellido}</h1>")

def saludo_template(request, nombre, apellido):
     # with open(r'C:\Users\User\OneDrive\Documentos\Coder Django\templates\saludo_template.html') as archivo_abierto:
    #     ...
    
    # archivo_abierto = open(r'C:\Users\User\OneDrive\Documentos\Coder Django\templates\saludo_template.html') #ABSOLUTA
    
    archivo_abierto = open(r'C:templates\saludo_template.html') # RELATIVA
    
    
    template = Template(archivo_abierto.read())
    
    archivo_abierto.close()
    
    fecha = datetime.now()
    datos = {
        'fecha': fecha.strftime('%H:%M:%S'),
        'nombre': nombre,
        'apellido': apellido
    }
    
    contexto = Context(datos)
    
    template_renderizado = template.render(contexto)
    

    return HttpResponse(template_renderizado)

def saludo_con_cargador(request, nombre, apellido):
    fecha = datetime.now()
    datos = {
        'fecha': fecha.strftime('%H:%M:%S'),
        'nombre': nombre,
        'apellido': apellido
    }
    
    # archivo_abierto = open(r'C:templates\saludo_template.html') # RELATIVA

    # template = Template(archivo_abierto.read())
    
    # archivo_abierto.close()
    
    template = loader.get_template(r'saludo_template.html')
    
    # contexto = Context(datos) No hace falta
    
    template_renderizado = template.render(datos)
    

    return HttpResponse(template_renderizado)

def saludo_con_render(request, nombre, apellido):
    fecha = datetime.now()
    datos = {
        'fecha': fecha.strftime('%H:%M:%S'),
        'nombre': nombre,
        'apellido': apellido
    }
    
    # template = loader.get_template(r'saludo_template.html')
    
    # template_renderizado = template.render(datos)
    

    # return HttpResponse(template_renderizado)
    
    return render(request,'inicio/saludo_template.html', datos)


def condicion_y_bucle(request):
    
    return render(request,'subcarpeta/condicion_y_bucle.html',{"listado_de_numeros":[1,2,4,5,33,2,4,5,3]})


def crear_auto(request, marca, modelo):
    
    auto1 = Auto(marca=marca, modelo=modelo)
    auto1.save()
    return render(request, 'inicio/crear_auto.html',{'auto1':auto1})