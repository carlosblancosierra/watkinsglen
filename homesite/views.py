from django.shortcuts import render
from .serializer import HomesiteSerializer
from .models import Homesite
from rest_framework import viewsets

# Create your views here.
class HomesiteListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Homesite.objects.all()
    serializer_class = HomesiteSerializer


