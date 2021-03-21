from django.shortcuts import render
from .models import *
# Create your views here.
#views based on functions (for now)
def index(request):
    return render(request, 'miblog/index.html', )

def programacion(request):
    return render(request, 'miblog/index.html', {'categorias': 1})

def pixelart(request):
    return render(request, 'miblog/index.html', {'categorias': 2})