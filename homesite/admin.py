from django.contrib import admin
from .models import Homesite

class HomesiteAdmin(admin.ModelAdmin):
    list_display = ('community', 'lot_number', 'address', 'status', 'sale_status')
    list_filter = ('status', 'sale_status')
    search_fields = ('community__name', 'lot_number')
    readonly_fields = ('community',)

admin.site.register(Homesite, HomesiteAdmin)
