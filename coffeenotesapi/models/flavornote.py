from django.db import models

class FlavorNote(models.Model):
    name = models.CharField(max_length=55)