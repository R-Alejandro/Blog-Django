from django.urls import path
from . import views

#generar las url para las vistas
app_name = 'miblog'
urlpatterns = [
    path('', views.index, name='index'),
    path('categoria/<int:cat_id>', views.programacion, name='prog'),
    path('post/<int:post_id>', views.post, name='post')
]
""" path('pixelart', views.pixelart, name='pixel'), """
""" path('<int:post_id>/post', views.post, name="post"), """