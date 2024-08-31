from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def menu(request):
    return render(request, 'core/menu.html')

def recuperacion(request):
    return render(request, 'core/recuperacion.html')

def recibido(request):
    return render(request, 'core/recibido.html')

