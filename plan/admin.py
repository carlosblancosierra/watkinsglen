from django.contrib import admin
from .models import Plan

# Register your models here.
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'sqft', 'rooms', 'bathrooms', 'half_baths', 'plan_library', 'active')
    list_filter = ('plan_library', 'active')
    search_fields = ('name',)
