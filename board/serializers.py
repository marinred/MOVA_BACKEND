from rest_framework import serializers
from board.models import Board


class BoardSerializer(serializers.ModelSerializer):
    board_user = serializers.SerializerMethodField()
    
    def get_board_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = Board
        fields = '__all__'

class BoardDetailSerializer(serializers.ModelSerializer):
    board_user = serializers.SerializerMethodField()
    
    def get_board_user(self, obj):
        return obj.user.username
    class Meta:
        model = Board
        fields = ("title", "content", "category","image", "webtoon","board_user",)