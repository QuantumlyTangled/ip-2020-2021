# Generated by Django 2.2.18 on 2021-02-17 07:40

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportaj_app', '0020_customtag_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtag',
            name='colour',
            field=colorfield.fields.ColorField(default='#2643E9FF', max_length=18),
        ),
    ]