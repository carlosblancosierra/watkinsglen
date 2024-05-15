from .views import CommunityListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'communities', CommunityListViewSet)
urlpatterns = router.urls

