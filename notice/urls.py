from django.urls import path
from notice import views


urlpatterns = [
    path('', views.NoticeView.as_view(), name='notice_view'),
    path('<int:notice_id>/', views.NoticeDetailView.as_view(), name='notice_detail_view'),
    path('all/', views.SearchAllView.as_view(), name='search_all_view'),
    path('notice/', views.SearchNoticeView.as_view(), name='search_notice_view'),
    path('event/', views.SearchEventView.as_view(), name='search_event_view'),
]