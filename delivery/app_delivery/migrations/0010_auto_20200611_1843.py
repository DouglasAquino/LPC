# Generated by Django 3.0.5 on 2020-06-11 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_delivery', '0009_pedido_atendido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='omplemento',
            new_name='complemento',
        ),
    ]