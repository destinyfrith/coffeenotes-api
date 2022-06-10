from django.db import models

class BrewingMethod(models.Model):
    type = models.CharField(max_length=55)