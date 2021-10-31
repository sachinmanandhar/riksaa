from django.contrib.gis.db import models

# Create your models here.

class RideRequest(models.Model):
    userId = models.IntegerField()
    
    loc = models.PointField()