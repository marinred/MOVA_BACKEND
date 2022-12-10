from django.urls import path
from notice import views


urlpatterns = [
    path('', views.NoticeView.as_view(), name='notice_view'),
    path('<int:notice_id>/', views.NoticeDetailView.as_view(), name='notice_detail_view'),
    path('all/', views.SearchNoticeView.as_view(), name='search_notice_view'),
]