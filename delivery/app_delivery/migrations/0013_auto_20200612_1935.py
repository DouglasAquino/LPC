# Generated by Django 3.0.5 on 2020-06-12 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_delivery', '0012_cesta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cesta',
            name='pedido',
        ),
        migrations.AddField(
            model_name='cesta',
            name='prato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_delivery.Prato'),
        ),
    ]
