from django.db import models


# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=100)
    floorplan = models.FileField(upload_to='floorplans/', null=True, blank=True)
    rendering = models.ImageField(upload_to='renderings/', null=True, blank=True)
    rooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    half_baths = models.PositiveIntegerField()

    def __str__(self):
        return self.name
