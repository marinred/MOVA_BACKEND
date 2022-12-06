from rest_framework import serializers
from notice.models import Notice

class NoticeSerializer(serializers.ModelSerializer):
    notice_user = serializers.SerializerMethodField()
    
    def get_notice_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = Notice
        fields = '__all__'