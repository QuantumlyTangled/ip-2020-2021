# Generated by Django 3.1.2 on 2020-10-18 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sportaj_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="klub",
            name="slug",
            field=models.SlugField(),
        ),
    ]
