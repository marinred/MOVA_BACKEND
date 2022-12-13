from rest_framework import serializers
from notice.models import Notice
    
class NoticeSerializer(serializers.ModelSerializer):
    notice_user = serializers.SerializerMethodField()
    notice_user_profile_image = serializers.SerializerMethodField()
    notice_category_name = serializers.SerializerMethodField()
    
    def get_notice_user(self, obj):
        return obj.user.username
    
    def get_notice_user_profile_image(self, obj):
        return obj.user.image.url
    
    def get_notice_category_name(self, obj):
        return obj.category_name.category_name
    
    class Meta:
        model = Notice
        fields = ("id","notice_user","notice_user_profile_image","title","content","created_at","updated_at","category_name", "notice_category_name")