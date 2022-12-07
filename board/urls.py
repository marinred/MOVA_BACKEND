from django.urls import path
from board import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.BoardView.as_view(), name='board_view'),
    path('<int:board_id>/', views.BoardDetailView.as_view(), name='board_detail_view'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
