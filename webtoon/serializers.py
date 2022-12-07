from rest_framework import serializers
from webtoon.models import Webtoon, WebtoonComment

class WebtoonViewSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    
    def get_likes_count(self, obj):
        return obj.webtoon_likes.count()
    
    class Meta:
        model = Webtoon
        fields = ('id', 'platform', 'author', 'title', 'genre', 'image_url', 'day_of_the_week', 'likes_count',)
        
class WebtoonDetailVeiwSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    bookmarks_count = serializers.SerializerMethodField()
    
    def get_likes_count(self, obj):
        return obj.webtoon_likes.count()
    def get_bookmarks_count(self, obj):
        return obj.webtoon_bookmarks.count()
    
    class Meta:
        model = Webtoon
        fields = ('id', 'platform', 'title', 'author', 'image_url', 'summary', 'genre', 'day_of_the_week', 'webtoon_link', 'likes_count', 'bookmarks_count',)
        
class WebtoonCommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    
    def get_username(self, obj):
        return obj.user.username
    
    class Meta:
        model = WebtoonComment
        fields = ('id', 'username', 'webtoon', 'content', 'created_at' , 'updated_at',)
        
class WebtoonCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebtoonComment
        fields = ('content',)