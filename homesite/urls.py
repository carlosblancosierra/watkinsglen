from .views import HomesiteListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'homesites', HomesiteListViewSet)
urlpatterns = router.urls

