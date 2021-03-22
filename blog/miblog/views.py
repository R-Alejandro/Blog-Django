from django.shortcuts import render
from .models import *
# Create your views here.
#views based on functions (for now)
def index(request):
    return render(request, 'miblog/index.html', )

def programacion(request):
    posts = Post.objects.filter(categoria_id_id=1)
    return render(request, 'miblog/prog.html', {'posts': posts})

def pixelart(request):
    posts = Post.objects.all()
    return render(request, 'miblog/pixel.html', {'posts': posts})