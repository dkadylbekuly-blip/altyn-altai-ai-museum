from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

from recognize.views import save_recognition


urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),

    # API без языкового префикса
    path("api/save-recognition/", save_recognition, name="api_save_recognition"),
]


urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("accounts/", include("accounts.urls")),
    path("recognize/", include(("recognize.urls", "recognize"), namespace="recognize")),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)