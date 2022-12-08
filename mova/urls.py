from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path("account/", include("django.contrib.auth.urls")),
    path("notice/", include("notice.urls")),
    path("board/", include("board.urls")),
    path("", include("webtoon.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

