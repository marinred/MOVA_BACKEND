from rest_framework import serializers
from fanart.models import BaseImage
from fanart.models import FanartImage
from fanart.models import Fanart
from user.models import User
from fanart.models import FanartComment
from uuid import uuid4

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
        fields = ('username','email')

class FanartGetListSerializer(serializers.ModelSerializer):
    image = FanartImageGetSerializer()
    user = UsersampleSerializer()
    class Meta:
        model = Fanart
        fields = '__all__'

class FanartGetSerializer(serializers.ModelSerializer):
    image = FanartImageGetSerializer()
    user = UsersampleSerializer()
    class Meta:
        model = Fanart
        fields = '__all__'

class FanartCommentCreateSerializer(serializers.ModelSerializer):
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