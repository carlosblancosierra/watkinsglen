from django.db import models

# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.name