from rest_framework import serializers
from webtoon.models import Webtoon

class WebtoonViewSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    
    def get_likes_count(self, obj):
        return obj.webtoon_likes.count()
    
    class Meta:
        model = Webtoon
        fields = ('id', 'platform', 'title', 'image_url', 'day_of_the_week', 'likes_count',)