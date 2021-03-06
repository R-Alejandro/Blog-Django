# Generated by Django 3.1.6 on 2021-03-17 08:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre de la categoria'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='numero_post',
            field=models.IntegerField(default=0, verbose_name='Numero de posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='autor_nombre',
            field=models.CharField(max_length=80, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='post',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='texto',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Titulo'),
        ),
    ]
