# Generated by Django 2.2.17 on 2021-01-27 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportaj_app', '0012_auto_20210127_2035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slikakluba',
            old_name='slike',
            new_name='slika',
        ),
    ]