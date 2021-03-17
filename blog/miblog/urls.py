from django.urls import path
from . import views

#generar las url para las vistas
urlpatterns = [
    path('', views.index, name='index'),
]