from django.shortcuts import render
from .models import Community
from .serializer import CommunitySerializer
from rest_framework import viewsets

# Create your views here.
class CommunityListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
