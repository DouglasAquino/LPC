# Generated by Django 3.0.5 on 2020-06-13 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_delivery', '0017_cesta_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='prato',
        ),
        migrations.AddField(
            model_name='pedido',
            name='cesta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_delivery.Cesta'),
        ),
    ]