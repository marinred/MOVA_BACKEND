from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from webtoon.models import Webtoon
from webtoon.serializers import WebtoonViewSerializer, WebtoonDetailVeiwSerializer

# Webtoon Mainpage
class WebtoonView(APIView):
    def get(self, request):
        
        # Today Webtoon View
        days=['월', '화', '수', '목', '금', '토', '일']
        a = datetime.datetime.today().weekday()
        today_webtoon = Webtoon.objects.filter(day_of_the_week=days[a])
        today_webtoon_serializer = WebtoonViewSerializer(today_webtoon, many=True)
        
        # Likes Webtoon View
        user = self.request.user
        bookmarks_webtoon = user.user_bookmarks.all()
        bookmarks_webtoon_serializer = WebtoonViewSerializer(bookmarks_webtoon, many=True)
        
        response_data = []
        response_data.append(today_webtoon_serializer.data)
        response_data.append(bookmarks_webtoon_serializer.data)
        return Response(response_data, status=status.HTTP_200_OK)

# Webtoon Detailpage
class WebtoonDetailVeiw(APIView):
    def get(self, request, webtoon_id):
        webtoon_detail = Webtoon.objects.get(id=webtoon_id)
        webtoon_detail_serializer = WebtoonDetailVeiwSerializer(webtoon_detail)
        return Response(webtoon_detail_serializer.data, status=status.HTTP_200_OK)

# Webtoon Like
class WebtoonLikeView(APIView):
    def post(self, request, webtoon_id):
        webtoon = get_object_or_404(Webtoon, id=webtoon_id)
        print(request.user)
        if request.user in webtoon.webtoon_likes.all():
            webtoon.webtoon_likes.remove(request.user)
            return Response("좋아요 취소 완료!", status=status.HTTP_200_OK)
        else:
            webtoon.webtoon_likes.add(request.user)
            return Response("좋아요 등록 완료!", status=status.HTTP_200_OK)

# Webtoon Bookmark
class WebtoonBookmarkView(APIView):
    def post(self, request, webtoon_id):
        webtoon = get_object_or_404(Webtoon, id=webtoon_id)
        print(request.user)
        if request.user in webtoon.webtoon_bookmarks.all():
            webtoon.webtoon_bookmarks.remove(request.user)
            return Response("북마크 취소 완료!", status=status.HTTP_200_OK)
        else:
            webtoon.webtoon_bookmarks.add(request.user)
            return Response("북마크 등록 완료!", status=status.HTTP_200_OK)