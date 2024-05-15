from .models import Gallery, GalleryImage, Image, ImageTag
from rest_framework import serializers

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ImageTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTag
        fields = '__all__'

