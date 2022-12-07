from django.urls import path
from board import views


urlpatterns = [
    path('', views.BoardView.as_view(), name='board_view'),
    path('<int:board_id>/', views.BoardDetailView.as_view(), name='board_detail_view'),
]