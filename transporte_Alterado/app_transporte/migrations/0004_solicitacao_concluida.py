# Generated by Django 3.0.5 on 2020-05-31 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_transporte', '0003_auto_20200531_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='concluida',
            field=models.BooleanField(default=False),
        ),
    ]
