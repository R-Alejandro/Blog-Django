from django.db import models
from ckeditor.fields import RichTextField #dependencia para texto xd
# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la categoria',max_length=100, null=False)
    estado = models.BooleanField('Estado',default=True)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now_add=True)
    numero_post = models.IntegerField('Numero de posts',default=0)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo',max_length=100, null=False, blank=False)
    #antes era textfield, pero se puede usar una dependencia, para poner
    #el cuadro de texto mas bonito
    texto = RichTextField()
    #texto = models.TextField(null=False, blank=False)
    imagen = models.URLField(max_length=255,blank=False,null=False, default='https://blog.aulaformativa.com/wp-content/uploads/2016/06/fondos-de-pantalla-para-programadores-CodeWallpaper3-702x336.jpg')
    fecha_creacion = models.DateField('Fecha de creacion',auto_now_add=True)
    autor_nombre = models.CharField('Autor', max_length=80, null=False, blank=False)
    categoria_id = models.ForeignKey('Categoria',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    