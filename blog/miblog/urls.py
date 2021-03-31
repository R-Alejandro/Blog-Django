from django.urls import path
from . import views

#generar las url para las vistas
app_name = 'miblog'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('categoria/<int:cat_id>', views.ListCategoria.as_view(), name='prog'),
    path('post/<int:post_id>', views.ShowPost.as_view(), name='post')
]
