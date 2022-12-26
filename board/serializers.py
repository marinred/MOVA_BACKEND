from rest_framework import serializers
from board.models import Board
from board.models import BoardComment
from webtoon.models import Webtoon

class WebtoonSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webtoon
        fields = ('title','id','image_url',"author",)
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
    comments_user_id = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username
    
    def get_user_profile_image(self, obj):
        return obj.user.image.url

    def get_comments_user_id(self, obj):
        return obj.user.id

    class Meta:
        model = BoardComment
        fields = ('id', 'comments_user_id', 'username', 'board', 'comment', 'created_at' , 'updated_at', 'user_profile_image',)

class BoardDetailSerializer(serializers.ModelSerializer):
    board_user_id = serializers.SerializerMethodField()
    board_user = serializers.SerializerMethodField()
    webtoon_title = serializers.SerializerMethodField()
    board_user_profile_image = serializers.SerializerMethodField()
    board_category_name = serializers.SerializerMethodField()
    
    def get_board_user_id(self, obj):
        return obj.user.id

    def get_board_user(self, obj):
        return obj.user.username
    
    def get_webtoon_title(self,obj):
        return obj.webtoon.title
    
    def get_board_user_profile_image(self, obj):
        return obj.user.image.url
    
    def get_board_category_name(self, obj):
        return obj.category_name.category_name
    class Meta:
        model = Board
        fields = ("id","board_user_id", "board_user","board_user_profile_image", "title", "content","category_name", "webtoon","webtoon_title","board_category_name","created_at","updated_at",)

class BoardCommentCreateSerializer(serializers.ModelSerializer):
    comments_user = serializers.SerializerMethodField()
    comments_board = serializers.SerializerMethodField()
    comments_user_id = serializers.SerializerMethodField()

    def get_comments_user(self, obj):
        return obj.user.username
    
    def get_comments_board(self, obj):
        return obj.board.id

    def get_comments_user_id(self, obj):
        return obj.user.id
    
    class Meta:
        model = BoardComment
        fields = ('id', 'comments_user_id', 'comment', 'comments_board', 'comments_user',)
