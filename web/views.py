from django.shortcuts import render, redirect
from .models import Flan
from .forms import ContactFormModelForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        'flanes': flanes_publicos
    }
    return render(request, 'index.html', context)

def acerca(request):
    return render(request, 'about.html')

@login_required
def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    
    if request.method == 'POST':
        flan_id = request.POST.get('flan_id')  # Obtén el ID del flan
        comentario_texto = request.POST.get('comentario')
        flan = get_object_or_404(Flan, id=flan_id)
        Comentario.objects.create(flan=flan, usuario=request.user, texto=comentario_texto)
        return redirect('bienvenido')

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

def flan_detalle(request, flan_id):
    flan = get_object_or_404(Flan, pk=flan_id)
    comentarios = Comentario.objects.filter(flan=flan).order_by('-fecha_creacion')
    return render(request, 'flan_detalle.html', {'flan': flan, 'comentarios': comentarios})