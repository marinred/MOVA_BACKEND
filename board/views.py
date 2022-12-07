from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from board.models import Board
from board.serializers import BoardSerializer


# Create your views here.
class BoardView(APIView):
    def get(self, request):
        pass
        board = Board.objects.all()
        serializer = BoardSerializer(board, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)