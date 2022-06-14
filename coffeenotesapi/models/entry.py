from django.db import models


class Entry(models.Model):
    name = models.CharField(max_length=75)
    image = models.URLField(max_length=500)
    brewing_method = models.ForeignKey(
        "BrewingMethod", on_delete=models.CASCADE)
    grind_setting = models.CharField(max_length=10)
    rating = models.CharField(max_length=5)
    flavor_profile = models.ManyToManyField(
        "FlavorNote")
    notes = models.CharField(max_length=200)
