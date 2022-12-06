from rest_framework import serializers
from fanart.models import BaseImage

class BaseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseImage
        fields = '__all__'

        extra_kwargs = {
            'image':{'read_only':True}
        }
