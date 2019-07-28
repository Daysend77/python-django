from django.db import models

# Create your models here.
class Station(models.Model):
    station_number = models.IntegerField()
    station_name = models.CharField(max_length=50)