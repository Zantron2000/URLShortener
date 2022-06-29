from django.db import models

# Create your models here.
class UrlShortener(models.Model):
    url = models.CharField(max_length=10000)
    short_link = models.CharField(max_length=10, unique=True)