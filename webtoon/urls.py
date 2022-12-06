from django.urls import path
from webtoon import views

urlpatterns = [
    path('', views.WebtoonView.as_view(), name='webtoon_view'),
]