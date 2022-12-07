from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from board.models import Board
from board.serializers import BoardSerializer
from board.serializers import BoardDetailSerializer

# Create your views here.
class BoardView(APIView):
    def get(self, request):
        pass
        board = Board.objects.all()
        serializer = BoardSerializer(board, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BoardDetailSerializer(data=request.data)
        print(serializer.initial_data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BoardDetailView(APIView):
    def get(self, request, board_id):
        board = Board.objects.get(id=board_id)
        serializer = BoardSerializer(board)
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
        
        