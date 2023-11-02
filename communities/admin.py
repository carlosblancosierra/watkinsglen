from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Add other fields as needed
