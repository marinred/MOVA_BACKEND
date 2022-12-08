from rest_framework import serializers
from notice.models import Notice
from notice.models import Category

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
class NoticeSerializer(serializers.ModelSerializer):
    notice_user = serializers.SerializerMethodField()
    
    def get_notice_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = Notice
        fields = '__all__'
        
class NoticeCreateSerializer(serializers.ModelSerializer):
    notice_user = serializers.SerializerMethodField()
    
    def get_notice_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = Notice
        fields = ("title", "content", "notice_user","category_name",)
    
    