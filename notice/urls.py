from django.urls import path
from notice import views


urlpatterns = [
    path('', views.NoticeView.as_view(), name='notice_view'),
]