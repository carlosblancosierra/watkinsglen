from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Homesite)
class HomesiteAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'lot_number', 'address', 'status', 'sale_status', 'hidden', 'lot_size', 'plan')
    list_filter = ('status', 'sale_status', 'hidden')
    search_fields = ('lot_number', 'address__street', 'address__community__name', 'plan__name')
