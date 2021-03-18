from django.urls import path
from . import views

#generar las url para las vistas
app_name = 'miblog'
urlpatterns = [
    path('', views.index, name='index'),
]