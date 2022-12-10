from rest_framework import serializers
from notice.models import Notice
    
class NoticeSerializer(serializers.ModelSerializer):
    notice_user = serializers.SerializerMethodField()
    notice_user_profile_image = serializers.SerializerMethodField()
    
    def get_notice_user(self, obj):
        return obj.user.username
    
    def get_notice_user_profile_image(self, obj):
        return obj.user.image.url
    
    class Meta:
        model = Notice
        fields = ("notice_user","notice_user_profile_image","title","content","created_at","updated_at","category_name")
    
    