from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from webtoon.models import Webtoon, WebtoonComment
from webtoon.serializers import WebtoonViewSerializer, WebtoonDetailVeiwSerializer, WebtoonCommentSerializer, WebtoonCommentCreateSerializer

# Webtoon Mainpage
class WebtoonView(APIView):
    def get(self, request):
        
        days=['월', '화', '수', '목', '금', '토', '일']
        a = datetime.datetime.today().weekday()
        
        # Naver Today Webtoon View
        naver_today_webtoon = Webtoon.objects.filter(day_of_the_week=days[a], platform="네이버")
        naver_today_webtoon_serializer = WebtoonViewSerializer(naver_today_webtoon, many=True)
        
        # Naver Today Webtoon View
        kakao_today_webtoon = Webtoon.objects.filter(day_of_the_week=days[a], platform="카카오")
        kakao_today_webtoon_serializer = WebtoonViewSerializer(kakao_today_webtoon, many=True)
        
        # Likes Webtoon View
        user = self.request.user
        bookmarks_webtoon = user.user_bookmarks.all()
        bookmarks_webtoon_serializer = WebtoonViewSerializer(bookmarks_webtoon, many=True)
        
        response_data = []
        response_data.append(naver_today_webtoon_serializer.data)
        response_data.append(kakao_today_webtoon_serializer.data)
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
        
class WebtoonCommentView(APIView):
    def get(self, request, webtoon_id):
        webtoon = Webtoon.objects.get(id=webtoon_id)
        comments = webtoon.webtoon_comment_set.all()
        serializer = WebtoonCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, webtoon_id):
        serializer = WebtoonCommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, webtoon_id=webtoon_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class WebtoonDetailCommentView(APIView):
    def put(self, request, webtoon_id, webtooncomment_id):
        comment = get_object_or_404(WebtoonComment, id=webtooncomment_id)
        if request.user == comment.user:
            serializer = WebtoonCommentCreateSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, webtoon_id, webtooncomment_id):
        comment = get_object_or_404(WebtoonComment, id=webtooncomment_id)
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)