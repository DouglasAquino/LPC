# Generated by Django 3.0.5 on 2020-06-12 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_delivery', '0015_auto_20200612_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cesta',
            name='cliente',
        ),
    ]
