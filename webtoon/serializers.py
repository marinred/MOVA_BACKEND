from rest_framework import serializers
from webtoon.models import Webtoon

class WebtoonViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Webtoon
        fields = ('id', 'platform', 'title', 'image_url', 'day_of_the_week',)