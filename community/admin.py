from django.contrib import admin
from .models import Community

class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'active', 'order')
    list_filter = ('active',)
    search_fields = ('name', 'city')

admin.site.register(Community, CommunityAdmin)
