from django.shortcuts import render
from .models import *
# Create your views here.
#views based on functions (for now)
def index(request):
    return render(request, 'miblog/index.html', )

def programacion(request, cat_id):
    posts = Post.objects.filter(categoria_id_id=cat_id)
    if cat_id == 1:
        tit = 'Programación'
    else:
        tit = 'Pixel Art'
    return render(request, 'miblog/prog.html', {'posts': posts, 'titulo': tit})

""" def pixelart(request):
    posts = Post.objects.filter(categoria_id_id=2)
    return render(request, 'miblog/pixel.html', {'posts': posts}) """

""" def post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.categoria_id_id
    return render(request, 'miblog/') """