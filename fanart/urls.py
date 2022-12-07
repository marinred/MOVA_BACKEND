from django.urls import path
from . import views

urlpatterns = [
    path("baseimage/", views.BaseImageView.as_view()),
    path("colorization/", views.ColorizationView.as_view()),
    path("", views.FanartView.as_view()),
    path("<int:fanart_id>", views.FanartView.as_view()),
    path("<int:fanart_id>/comment/", views.FanartCommentView.as_view())
]
