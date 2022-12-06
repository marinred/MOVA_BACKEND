from django.urls import path
from webtoon import views

urlpatterns = [
    path('', views.WebtoonView.as_view(), name='webtoon_view'),
    path('<int:webtoon_id>/', views.WebtoonDetailVeiw.as_view(), name='webtoon_detail_view'),
    path('<int:webtoon_id>/like/', views.WebtoonLikeView.as_view(), name='webtoon_like_view'),
    path('<int:webtoon_id>/bookmark/', views.WebtoonBookmarkView.as_view(), name='webtoon_bookmark_view'),
    path('<int:webtoon_id>/comment/', views.WebtoonCommentView.as_view(), name='webtoon_comment_view'),
    path('<int:webtoon_id>/comment/<int:webtooncomment_id>/', views.WebtoonDetailCommentView.as_view(), name='webtoon_comment_detail_view'),
]