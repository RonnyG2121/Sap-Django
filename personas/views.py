from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import Persona
from .forms import Form_persona

# Create your views here.


def detalle_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    context = {
        'persona': persona
    }

    return render(request, 'personas/detalle_persona.html', context)

# Form_persona = modelform_factory(Persona, exclude=[])


def nueva_persona(request):
    if request.method == 'POST':
        crea_persona = Form_persona(request.POST)
        if crea_persona.is_valid():
            crea_persona.save()
            return redirect('index')

    else:
        crea_persona = Form_persona()

    return render(request, "personas/nuevo.html",
                  {"crea_persona": crea_persona})


def editar(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        crea_persona = Form_persona(request.POST, instance=persona)
        if crea_persona.is_valid():
            crea_persona.save()
            return redirect('index')

    else:
        crea_persona = Form_persona(instance=persona)

    return render(request, "personas/editar.html",
                  {"crea_persona": crea_persona})

def eliminar(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')