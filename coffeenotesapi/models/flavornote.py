from django.db import models

class FlavorNotes(models.Model):
    name = models.CharField(max_length=55)