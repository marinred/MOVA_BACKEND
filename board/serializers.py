from rest_framework import serializers
from board.models import Board
from board.models import BoardComment
from webtoon.models import Webtoon

class WebtoonSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webtoon
        fields = ('title','id','image_url',)
class BoardSerializer(serializers.ModelSerializer):
    board_user = serializers.SerializerMethodField()
    
    def get_board_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = Board
        fields = '__all__'

class BoardCommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    user_profile_image = serializers.SerializerMethodField()
    
    def get_username(self, obj):
        return obj.user.username
    
    def get_user_profile_image(self, obj):
        return obj.user.image.url
    class Meta:
        model = BoardComment
        fields = ('id', 'username', 'board', 'comment', 'created_at' , 'updated_at', 'user_profile_image',)

class BoardDetailSerializer(serializers.ModelSerializer):
    board_user = serializers.SerializerMethodField()
    webtoon_title = serializers.SerializerMethodField()
    
    def get_board_user(self, obj):
        return obj.user.username
    
    def get_webtoon_title(self,obj):
        return obj.webtoon.title
    class Meta:
        model = Board
        fields = ("title", "content","image", "webtoon","board_user","category_name","webtoon_title",)

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