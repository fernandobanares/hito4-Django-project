from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def acerca(request):
    return render(request, 'about.html')

def bienvenido(request):
    return render(request, 'welcome.html')
