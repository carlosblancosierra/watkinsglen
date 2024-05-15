from django.shortcuts import render
from .models import Gallery, GalleryImage, Image, ImageTag
from .serializer import GallerySerializer, GalleryImageSerializer, ImageSerializer, ImageTagSerializer
from rest_framework import viewsets

# Create your views here.
class GalleryListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class GalleryImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer

class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageTagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ImageTag.objects.all()
    serializer_class = ImageTagSerializer
