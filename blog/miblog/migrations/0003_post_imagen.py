# Generated by Django 3.1.6 on 2021-03-22 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miblog', '0002_auto_20210317_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.URLField(default='https://blog.aulaformativa.com/wp-content/uploads/2016/06/fondos-de-pantalla-para-programadores-CodeWallpaper3-702x336.jpg', max_length=255),
        ),
    ]