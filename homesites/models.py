from django.db import models

from addresses.models import Address
from communities.models import Community
from plans.models import Plan


# Create your models here.
class Homesite(models.Model):
    # community = models.ForeignKey(Community, on_delete=models.CASCADE, null=True, blank=True)
    lot_number = models.IntegerField(null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    listing_picture = models.ImageField(upload_to='listings/', null=True, blank=True)
    rendering = models.ImageField(upload_to='renderings/', null=True, blank=True)
    aerial_shot = models.ImageField(upload_to='aerial_shots/', null=True, blank=True)
    STATUS_CHOICES = [
        ('presale', 'Available for Presale'),
        ('coming', 'Coming Soon'),
        ('construction', 'Under Construction'),
        ('ready', 'Move-in Ready'),
    ]
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, null=True, blank=True)
    SALE_STATUS_CHOICES = [
        ('available', 'Available'),
        ('contract', 'Under Contract'),
        ('sold', 'Sold'),
    ]
    sale_status = models.CharField(max_length=10, choices=SALE_STATUS_CHOICES, null=True, blank=True)
    hidden = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    lot_size = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def community(self):
        if self.address:
            return self.address.community
        return None

    def __str__(self):
        return f"{self.community} - Lot {self.lot_number}"

    class Meta:
        ordering = ['lot_number']
