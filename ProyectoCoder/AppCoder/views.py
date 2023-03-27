from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante, Profesor, Entregable


# Create your views here.

def curso(self):
    curso = Curso(nombre="Desarrollo Web", camada="19881")
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre} Camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)

from django.http import HttpResponse

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def cursoFormulario(request):

    if request.method == "POST":

        curso = Curso(nombre=request.POST["curso"], camada=(request.POST["camada"]))
        
        curso.save()

        return render(request, "AppCoder/inicio.html")
    return render(request, "AppCoder/cursoFormulario.html")

def estudianteFormulario(request):

    if request.method == "POST":

        estudiante = Estudiante(nombre=request.POST["nombre"], apellido=(request.POST["apellido"]), email=request.POST["email"])
        
        estudiante.save()

        return render(request, "AppCoder/inicio.html")
    return render(request, "AppCoder/estudianteFormulario.html")


def profesorFormulario(request):

    if request.method == "POST":

        profesor = Profesor(nombre=request.POST["nombre"], apellido=(request.POST["apellido"]), email=request.POST["email"], profesion=request.POST["profesion"])
        
        profesor.save()

        return render(request, "AppCoder/inicio.html")
    return render(request, "AppCoder/profesorFormulario.html")


def entregableFormulario(request):
        
        if request.method == "POST":

            entregable = Entregable(nombre=request.POST["nombre"], fechaDeEntrega=(request.POST["fechaEntrega"]), entregado=request.POST["entregado"])
        
            entregable.save()

            return render(request, "AppCoder/inicio.html")
        return render(request, "AppCoder/entregableFormulario.html")

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")


def buscar(request):

    if request.GET["camada"]:

        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos, "camada":camada})
    
    else:
        respuesta = "No enviaste datos."
    
    return HttpResponse(respuesta)