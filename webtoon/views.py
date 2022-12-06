from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from webtoon.models import Webtoon
from webtoon.serializers import WebtoonViewSerializer, WebtoonDetailVeiwSerializer
import datetime

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