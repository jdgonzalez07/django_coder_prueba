from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Auto
from inicio.forms import FormularioCrearAuto, FormularioBusqueda

def inicio(request):
    # return HttpResponse("<h1>Estoy en el inicio</h1>")
    return render(request, 'inicio/index.html')


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


def crear_auto(request):
    
    print("###################################")
    print("###################################")
    print(request.GET)
    print("###################################")
    print("###################################")
    print(request.POST)
    
    # SIN FORMULARIOS DE DJANGO
    # if request.method == 'POST':
    #     auto1 = Auto(marca=request.POST['marca'], modelo=request.POST['modelo'])
    #     auto1.save()
        
    #     return render(request, 'inicio/creacion_finalizada.html',{'auto':auto1})
        
    # return render(request, 'inicio/crear_auto.html',{})
    
    
    # CON FORMULARIO DE DJANGO
    # FormularioCrearAuto
    
    if request.method == "POST":
        formulario = FormularioCrearAuto(request.POST)
        if formulario.is_valid():
            nueva_data = formulario.cleaned_data
            auto1 = Auto(marca=nueva_data['marca'], modelo=nueva_data['modelo'])
            auto1.save()
            return render(request, 'inicio/creacion_finalizada.html',{'auto':auto1})
    else:
        formulario = FormularioCrearAuto()
        return render(request, 'inicio/crear_auto.html', {'formulario':formulario})


def listado_autos(request):
    formulario = FormularioBusqueda(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data['marca']
        modelo_a_buscar = formulario.cleaned_data['modelo']
        autos = Auto.objects.filter(marca__icontains = marca_a_buscar, modelo__icontains = modelo_a_buscar)
    
    
    return render(request, 'inicio/listado_autos.html', {'autos':autos, 'formulario':formulario})