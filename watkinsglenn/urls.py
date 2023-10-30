from django.contrib import admin
from django.urls import path
from django.conf import settings

from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('admin/', admin.site.urls),
]


if settings.STATIC_LOCAL:
    # test mode
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
