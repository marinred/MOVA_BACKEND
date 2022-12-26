from django.urls import path
from webtoon import views

urlpatterns = [
    path('', views.WebtoonView.as_view(), name='webtoon_view'),
    path('all/', views.AllWebtoonView.as_view(), name='all_webtoon'),
    path('hotmova/', views.HotMovaView.as_view(), name='hotmova_webtoon'),
    path('naver/', views.NaverWebtoonView.as_view(), name='naver_webtoon'),
    path('naverend/', views.NaverEndWebtoonView.as_view(), name='naver_end_webtoon'),
    path('kakao/', views.KakaoWebtoonView.as_view(), name='kakao_webtoon'),
    path('kakaoend/', views.KakaoendWebtoonView.as_view(), name='kakao_end_webtoon'),
    path('<int:webtoon_id>/', views.WebtoonDetailVeiw.as_view(), name='webtoon_detail_view'),
    path('<int:webtoon_id>/like/', views.WebtoonLikeView.as_view(), name='webtoon_like_view'),
    path('<int:webtoon_id>/bookmark/', views.WebtoonBookmarkView.as_view(), name='webtoon_bookmark_view'),
    path('<int:webtoon_id>/comment/', views.WebtoonCommentView.as_view(), name='webtoon_comment_view'),
    path('<int:webtoon_id>/comment/<int:webtooncomment_id>/', views.WebtoonDetailCommentView.as_view(), name='webtoon_comment_detail_view'),
]
