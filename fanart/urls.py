from django.urls import path
from . import views

urlpatterns = [
    path("baseimage/", views.BaseImageView.as_view()),
]
