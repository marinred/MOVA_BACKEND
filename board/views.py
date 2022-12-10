from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from board.pagination import BoardPagination
from board.pagination import WebtoonPagination
from rest_framework import status
from rest_framework.response import Response
from board.models import Board
from webtoon.models import Webtoon
from board.models import BoardComment
from board.serializers import BoardDetailSerializer
from board.serializers import BoardCommentSerializer
from board.serializers import BoardCommentCreateSerializer
from board.serializers import WebtoonSearchSerializer
# Create your views here.
class BoardView(APIView):
    def post(self, request):
        serializer = BoardDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BoardDetailView(APIView):
    def get(self, request, board_id):
        board = Board.objects.get(id=board_id)
        serializer = BoardDetailSerializer(board)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, board_id):
        board = Board.objects.get(id=board_id)
        if request.user == board.user:
            serializer = BoardDetailSerializer(board, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 존재하지 않습니다.", status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request, board_id):
        board = Board.objects.get(id=board_id)
        if request.user == board.user:
            board.delete()
            return Response("삭제가 완료되었습니다.", status=status.HTTP_200_OK)
        else:
            return Response("권한이 존재하지 않습니다.", status=status.HTTP_403_FORBIDDEN)
        

class BoardCommentView(APIView):
    def get(self, request, board_id):
        board = Board.objects.get(id=board_id)
        comments = board.board_comment_set.all()
        serializer = BoardCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, board_id):
        serializer = BoardCommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, board_id=board_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class BoardCommentDetailView(APIView):
    def put(self, request, board_id, boardcomment_id):
        comment = BoardComment.objects.get(id=boardcomment_id)
        if request.user == comment.user:
            serializer = BoardCommentCreateSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response("권한이 존재하지 않습니다.", status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request, board_id, boardcomment_id):
        comment = BoardComment.objects.get(id=boardcomment_id)
        if request.user == comment.user:
            comment.delete()
            return Response("삭제가 완료되었습니다.", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 존재하지 않습니다.", status=status.HTTP_403_FORBIDDEN)
            
            
class SearchBoardView(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer
    pagination_class = BoardPagination
    filter_backends = [SearchFilter]
    search_fields = ('title',)
    
class SearchWebtoonView(ListAPIView):
    queryset = Webtoon.objects.all()
    serializer_class = WebtoonSearchSerializer
    pagination_class = WebtoonPagination
    filter_backends = [SearchFilter]
    search_fields = ('title',)
    
    
class CreateBoardView(APIView):
    def post(self, request):
        serializer = BoardDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)