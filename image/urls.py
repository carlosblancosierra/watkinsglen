from .views import GalleryImageViewSet, GalleryListViewSet, ImageTagViewSet, ImageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'images', ImageViewSet)
router.register(r'images/tags', ImageTagViewSet)
router.register(r'images/galleries', GalleryListViewSet)

urlpatterns = router.urls

