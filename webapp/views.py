from django.shortcuts import render, HttpResponse
from personas.models import Persona

# Create your views here.

def bienvenida(request):
    num_personas = Persona.objects.count()
    personas = Persona.objects.order_by("id")

    context = {
        "num_personas": num_personas,
        "personas": personas
    }

    return render(request, "bienvenida.html", context)

"""def contacto(request):
    return HttpResponse("Correo: micorreo@mail.com. Teléfono: 12345456765433")

def despedirse(request):
    return HttpResponse("Despedida desde Django")"""