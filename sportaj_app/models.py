from django.db import models

import os
from PIL import Image
from geopy.geocoders import Nominatim
from location_field.models.plain import PlainLocationField

from .tags import custom_tag_field


geolocator = Nominatim(user_agent="sportaj.ga")


def get_header_images_default(): list([])


def get_location_city_default():
    return "46.55472,15.64667"

PanogeManager = custom_tag_field("sportaj_app", "Klub", "Panoga", "panoge")
VadbeManager = custom_tag_field("sportaj_app", "Klub", "Vadba", "vadbe")
StarostiManager = custom_tag_field("sportaj_app", "Klub", "Starost", "starosti")
SpoliManager = custom_tag_field("sportaj_app", "Klub", "Spol", "spoli")


class Klub(models.Model):
    slug = models.SlugField(unique=True)

    ime = models.CharField(max_length=512)
    opis = models.CharField(max_length=4096)

    logo = models.ImageField(upload_to="klub_logo/", blank=True)

    location = PlainLocationField(default=get_location_city_default())
    location_friendly = models.CharField(max_length=4096, null=True, blank=True)

    urnik = models.CharField(max_length=512, null=True, blank=True)

    mail = models.EmailField(null=True, blank=True)
    homepage = models.URLField(null=True, blank=True)

    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)

    panoge_tags = PanogeManager
    vadbe_tags = VadbeManager
    starosti_tags = StarostiManager
    spoli_tags = SpoliManager

    class Meta:
        verbose_name = "Klub"
        verbose_name_plural = "Klubi"

    def save(self, *args, **kwargs):
        super(Klub, self).save(*args, **kwargs)

        logo = Image.open(self.logo.path).convert("RGB")
        logo.save(os.path.splitext(self.logo.path)[0] + ".webp", "webp", lossless=False, quality=75)

        self.logo = os.path.splitext(self.logo.name)[0] + ".webp"
        self.location_friendly = geolocator.reverse(self.location).address
        super(Klub, self).save(*args, **kwargs)

    def __str__(self):
        return self.ime


class SlikaKluba(models.Model):
    naslov = models.CharField(max_length=512)
    opis = models.CharField(max_length=4096)
    slika = models.ImageField(upload_to="header_slike/")

    klub = models.ForeignKey(Klub, on_delete=models.CASCADE, related_name="slike")

    class Meta:
        verbose_name = "Slika"
        verbose_name_plural = "Slike"

    def save(self, *args, **kwargs):
        super(SlikaKluba, self).save(*args, **kwargs)

        image = Image.open(self.slika.path).convert("RGB")
        image.save(os.path.splitext(self.slika.path)[0] + ".webp", "webp", lossless=False, quality=50)

        self.slika = os.path.splitext(self.slika.name)[0] + ".webp"
        super(SlikaKluba, self).save(*args, **kwargs)

    def __str__(self):
        return "%s - %s" % (self.klub, self.naslov)
