# Generated by Django 3.0.5 on 2020-06-08 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_delivery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrega',
            name='cliente',
        ),
    ]
