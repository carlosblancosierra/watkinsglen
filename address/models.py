from django.db import models

# Create your models here.
class Address(models.Model):
    street_number = models.CharField(max_length=10)  # Add street number field
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street_number} {self.street}, {self.city}, {self.state} {self.zipcode}"

    @property
    def short(self):
        return f"{self.street_number} {self.street}"
