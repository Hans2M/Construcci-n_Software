# Generated by Django 5.1.3 on 2024-12-18 22:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_lugar_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='lugar',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
