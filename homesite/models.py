from django.db import models

from address.models import Address
from community.models import Community
from image.models import Image, Gallery
from plan.models import Plan
from .enumeration import HomesiteStatus, HomesiteSaleStatus

# Create your models here.
class Homesite(models.Model):
    community = models.ForeignKey(Community, on_delete=models.PROTECT, null=True, blank=True)
    lot_number = models.IntegerField(null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True, blank=True)
    listing_picture_landscape = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, blank=True, related_name='listing_picture_landscape')
    listing_picture_portrait = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, blank=True, related_name='listing_picture_portrait')
    status = models.CharField(max_length=50, choices=HomesiteStatus.values(), default=HomesiteStatus.LOT.value)
    sale_status = models.CharField(max_length=50, choices=HomesiteSaleStatus.values(), default=HomesiteSaleStatus.AVAILABLE.value)

    construction_gallery = models.ForeignKey(Gallery, on_delete=models.PROTECT, null=True, blank=True, related_name='construction_gallery')
    move_in_ready_gallery = models.ForeignKey(Gallery, on_delete=models.PROTECT, null=True, blank=True, related_name='move_in_ready_gallery')
    lot_gallery = models.ForeignKey(Gallery, on_delete=models.PROTECT, null=True, blank=True, related_name='lot_gallery')

    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, null=True, blank=True)

    featured = models.BooleanField(default=False)
    lot_size = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.community} - Lot {self.lot_number} - {self.address.short}"

    class Meta:
        ordering = ['lot_number']
