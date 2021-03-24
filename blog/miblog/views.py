from django.shortcuts import render
from .models import *
# Create your views here.
#views based on functions (for now)
def index(request):
    return render(request, 'miblog/index.html', )

def programacion(request, cat_id):
    posts = Post.objects.filter(categoria_id_id=cat_id)
    tit = Categoria.objects.get(id=cat_id)
    tit = tit.nombre
    return render(request, 'miblog/prog.html', {'posts': posts, 'titulo': tit})


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    banner = Categoria.objects.get(id=post.categoria_id_id)
    banner = banner.nombre
    return render(request, 'miblog/post.html', {'post': post, 'banner': banner})