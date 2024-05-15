from django.contrib import admin
from .models import ImageTag, Image, Gallery, GalleryImage

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage

@admin.register(ImageTag)
class ImageTagAdmin(admin.ModelAdmin):
    list_display = ('tag',)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'display_tags')
    def display_tags(self, obj):
        return ", ".join([tag.tag for tag in obj.tags.all()])

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('gallery', 'image', 'order')
    list_filter = ('gallery',)
