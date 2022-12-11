from rest_framework import serializers
from fanart.models import BaseImage
from fanart.models import FanartImage
from fanart.models import Fanart
from user.models import User
from fanart.models import FanartComment

class BaseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseImage
        fields = '__all__'

        extra_kwargs = {
            'image':{'read_only':True}
        }

class FanartImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FanartImage
        fields = ('id','resize_image','hint_image')

        # extra_kwargs = {
        #     'resize_image':{'read_only':True}
        # }

class FanartImageCreateSerializer(serializers.ModelSerializer):
    result_image = serializers.StringRelatedField()

    class Meta:
        model = FanartImage
        fields = '__all__'
        extra_kwargs = {
            'resize_image':{'read_only':True},
            'hint_image':{'read_only':True},
        }

class FanartImageGetSerializer(serializers.ModelSerializer):
    resize_image = BaseImageSerializer()
    class Meta:
        model = FanartImage
        fields = '__all__'

class FanartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fanart
        fields = '__all__'
        extra_kwargs = {
            'user':{'read_only':True},
            'likes': {'required': False},
        }

class UsersampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','image')

class FanartGetListSerializer(serializers.ModelSerializer):
    image = FanartImageGetSerializer()
    user = UsersampleSerializer()
    class Meta:
        model = Fanart
        fields = '__all__'

class FanartCommentSerializer(serializers.ModelSerializer):
    user = UsersampleSerializer()
    class Meta:
        model = FanartComment
        fields = '__all__'
    

class FanartGetSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    user = UsersampleSerializer()
    comment_set = serializers.SerializerMethodField()

    def get_image(self, obj):
        return obj.image.result_image.url
    class Meta:
        model = Fanart
        fields = '__all__'
    def get_comment_set(self, instance):
        queryset = instance.comment_set.order_by('-created_at')
        return FanartCommentSerializer(queryset, many=True).data

class FanartCommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self,obj):
        return obj.user.username
    class Meta:
        model = FanartComment
        fields = '__all__'
        extra_kwargs = {
            'user':{'read_only':True},
            'fanart':{'read_only':True},
        }

class FanartPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = FanartComment
        fields = ('content','updated_at')