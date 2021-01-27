# Generated by Django 2.2.17 on 2021-01-27 14:39

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('sportaj_app', '0009_klub_twitter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='klub',
            name='city',
        ),
        migrations.AlterField(
            model_name='klub',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='46.55472,15.64667', max_length=63),
        ),
    ]
