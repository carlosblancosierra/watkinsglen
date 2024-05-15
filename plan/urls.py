from .views import PlanListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'plans', PlanListViewSet)
urlpatterns = router.urls

