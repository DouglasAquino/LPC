# Generated by Django 3.0.3 on 2020-03-07 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_noticias', '0002_comentarios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentarios',
            old_name='com',
            new_name='comentario',
        ),
    ]
