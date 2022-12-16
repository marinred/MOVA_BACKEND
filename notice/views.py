from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from notice.models import Notice
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from notice.pagination import NoticePagination
from notice.serializers import NoticeSerializer


# Create your views here.

class NoticeView(APIView):
    def post(self, request):
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoticeDetailView(APIView):
    def get(self, request, notice_id):
        notice = Notice.objects.get(id=notice_id)
        serializer = NoticeSerializer(notice)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, notice_id):
        notice = Notice.objects.get(id=notice_id)
        if request.user == notice.user:
            serializer = NoticeSerializer(notice, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 존재하지 않습니다.", status=status.HTTP_403_FORBIDDEN)
            
    def delete(self, request, notice_id):
        notice = Notice.objects.get(id=notice_id)
        if request.user == notice.user:
            notice.delete()
            return Response("삭제가 완료되었습니다.", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 존재하지 않습니다.", status=status.HTTP_403_FORBIDDEN)
        
class SearchAllView(ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    pagination_class = NoticePagination
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ('id',)
    search_fields = ('title',)
    
class SearchNoticeView(ListAPIView):
    queryset = Notice.objects.filter(category_name="1")
    serializer_class = NoticeSerializer
    pagination_class = NoticePagination
    filter_backends = [OrderingFilter]
    ordering_fields = ('id',)
    
class SearchEventView(ListAPIView):
    queryset = Notice.objects.filter(category_name="2")
    serializer_class = NoticeSerializer
    pagination_class = NoticePagination
    filter_backends = [OrderingFilter]
    ordering_fields = ('id',)