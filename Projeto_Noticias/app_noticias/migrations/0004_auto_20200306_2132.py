# Generated by Django 3.0.3 on 2020-03-07 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_noticias', '0003_auto_20200306_2129'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comentarios',
            new_name='Comentario',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='comentario',
            new_name='comentari',
        ),
    ]
