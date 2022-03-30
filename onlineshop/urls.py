from django.contrib import admin
from django.urls import path, include
from django.urls import reverse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("store.urls")),
    path("shopping/", include("shopping.urls")),
    path("accounts/", include("accounts.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)