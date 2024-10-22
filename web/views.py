from django.shortcuts import render, redirect
from .models import Flan
from .forms import ContactFormModelForm
from django.http import HttpResponseRedirect

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        'flanes': flanes_publicos
    }
    return render(request, 'index.html', context)

def acerca(request):
    return render(request, 'about.html')

def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'flanes': flanes_privados
    }
    return render(request, 'welcome.html', context)

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el contacto en la base de datos
            return redirect('exito')  # Redirigir a la página de éxito
    else:
        form = ContactFormModelForm()  # Mostrar formulario vacío
    return render(request, 'contactus.html', {'form': form})

def exito(request):
    return render(request, 'success.html', {'message': "Gracias por contactarte con OnlyFlans, te responderemos en breve."})
