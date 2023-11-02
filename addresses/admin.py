from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street_number', 'street', 'city', 'state', 'zipcode', 'community')
    list_filter = ('community',)  # Add other fields as needed
