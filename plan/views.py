from .models import Plan
from .serializer import PlanSerializer
from rest_framework import viewsets

# Create your views here.
class PlanListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
