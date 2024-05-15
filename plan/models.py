from django.db import models

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=100)
    floorplan = models.FileField(upload_to='floorplans/', null=True, blank=True)
    rendering = models.ImageField(upload_to='renderings/', null=True, blank=True)
    sqft = models.PositiveIntegerField(null=True, blank=True)
    rooms = models.PositiveIntegerField(null=True, blank=True)
    bathrooms = models.PositiveIntegerField(null=True, blank=True)
    half_baths = models.PositiveIntegerField(null=True, blank=True)
    plan_library = models.BooleanField(default=False)
    gallery = models.ForeignKey('image.Gallery', on_delete=models.PROTECT, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
