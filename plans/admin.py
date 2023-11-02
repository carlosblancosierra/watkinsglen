from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'rooms', 'bathrooms', 'half_baths')
