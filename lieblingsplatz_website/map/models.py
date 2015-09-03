from django.db import models


class Kita(models.Model):
 name = models.TextField()
 latitude = models.FloatField()
 longitude = models.FloatField()
 address = models.TextField()
 zip_code = models.IntegerField()
 district = models.TextField()
 senats_id = models.IntegerField()
