# Generated by Django 3.1.2 on 2020-11-03 21:35

import django.contrib.postgres.fields
from django.db import migrations, models
import sportaj_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('sportaj_app', '0003_auto_20201018_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='klub',
            name='Header Images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(default=''), default=sportaj_app.models.get_header_images_default, size=None, verbose_name='header_images'),
        ),
    ]
