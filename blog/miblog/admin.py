from django.contrib import admin
from .models import *
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre'] #añade barra de busqueda
    #muestra en el sitio de admin el contenido de estas variables
    list_display = ('nombre','numero_post','fecha_creacion','estado',)

class PostAdmin(admin.ModelAdmin):
    search_fields = ['titulo','fecha_creacion','autor_nombre']
    list_display = ('titulo','fecha_creacion','autor_nombre')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
