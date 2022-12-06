from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from webtoon.models import Webtoon
from webtoon.serializers import WebtoonViewSerializer, WebtoonDetailVeiwSerializer

class WebtoonView(APIView):
    def get(self, request):
        days=['월', '화', '수', '목', '금', '토', '일']
        a = datetime.datetime.today().weekday()
        webtoon = Webtoon.objects.filter(day_of_the_week=days[a])
        webtoon_serializer = WebtoonViewSerializer(webtoon, many=True)
        return Response(webtoon_serializer.data, status=status.HTTP_200_OK)
    
class WebtoonDetailVeiw(APIView):
    def get(self, request, webtoon_id):
        webtoon_detail = Webtoon.objects.get(id=webtoon_id)
        webtoon_detail_serializer = WebtoonDetailVeiwSerializer(webtoon_detail)
        return Response(webtoon_detail_serializer.data, status=status.HTTP_200_OK)
    
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