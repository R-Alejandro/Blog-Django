from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from django.views.generic import TemplateView, ListView
# Create your views here.

class Index(TemplateView): #view based on class
    template_name = 'miblog/index.html'

class ListCategoria(ListView):
    template_name = 'miblog/prog.html'
    paginate_by = 2
    
    def get_queryset(self):
        posts = Post.objects.filter(categoria_id_id=self.kwargs['cat_id'])
        return posts.order_by('-fecha_creacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.get_queryset()
        context['titulo'] = Categoria.objects.get(id=self.kwargs['cat_id']).nombre 
        return context 

"""Vista basada en funcion, esta deshabilitada en urls.py"""
def programacion(request, cat_id):
    posts = Post.objects.filter(categoria_id_id=cat_id)
    posts = posts.order_by('-fecha_creacion')
    paginator = Paginator(posts, 2) #numero de objetos por pagina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    tit = Categoria.objects.get(id=cat_id)
    tit = tit.nombre
    content = {'posts': posts, 'titulo': tit, 'pg_obj':page_obj}
    return render(request, 'miblog/prog.html', content)

class ShowPost(TemplateView):
    template_name = 'miblog/post.html'
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.model.objects.get(id=self.kwargs['post_id'])
        context['banner'] = Categoria.objects.get(id=context['post'].categoria_id_id).nombre
        return context 

"""Vista basada en funcion, esta deshabilitada en urls.py"""
def post(request, post_id):
    post = Post.objects.get(id=post_id)
    banner = Categoria.objects.get(id=post.categoria_id_id)
    banner = banner.nombre
    return render(request, 'miblog/post.html', {'post': post, 'banner': banner})