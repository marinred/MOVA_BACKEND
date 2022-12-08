from rest_framework import serializers
from board.models import Board
from board.models import BoardComment


class BoardSerializer(serializers.ModelSerializer):
    board_user = serializers.SerializerMethodField()
    
    def get_board_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = Board
        fields = '__all__'

class BoardCommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    
    def get_username(self, obj):
        return obj.user.username  
    class Meta:
        model = BoardComment
        fields = ('id', 'username', 'board', 'comment', 'created_at' , 'updated_at',)

class BoardDetailSerializer(serializers.ModelSerializer):
    board_user = serializers.SerializerMethodField()
    board_comment_set = BoardCommentSerializer(many=True)
    
    def get_board_user(self, obj):
        return obj.user.username
    class Meta:
        model = Board
        fields = ("title", "content", "category","image", "webtoon","board_user","board_comment_set",)
    

class BoardCommentCreateSerializer(serializers.ModelSerializer):
    comments_user = serializers.SerializerMethodField()
    comments_board = serializers.SerializerMethodField()
    
    def get_comments_user(self, obj):
        return obj.user.username
    
    def get_comments_board(self, obj):
        return obj.board.id
    
    class Meta:
        model = BoardComment
        fields = ('comment', 'comments_board', 'comments_user',)