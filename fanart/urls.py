from django.urls import path
from . import views

urlpatterns = [
    path("baseimage/", views.BaseImageView.as_view()),
    path("colorization/", views.ColorizationView.as_view()),
    path("", views.FanartListView.as_view()),
    path("search/<int:webtoon_id>/",views.FanartWebtoonListView.as_view()),
    path("<int:fanart_id>/", views.FanartView.as_view()),
    path("<int:fanart_id>/comment/", views.FanartCommentView.as_view()),
    path("<int:fanart_id>/comment/<int:comment_id>", views.FanartCommentView.as_view()),
    path("<int:fanart_id>/like/", views.FanartLike.as_view())
]
