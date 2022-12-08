from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import User
#from webtoon.serializers import WebtoonSerializer

# 회원가입
class UserSerializer(serializers.ModelSerializer):
    #image = serializers.ImageField(user_url=True)
    
    class Meta:
        model = User
        fields = "__all__"
        
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

# 로그인 
class CustomObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email

        return token

# 프로필 
class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "bio" , "image")
        
# 프로필 수정
class UserProfileUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "bio" , "image")
    
    extra_kwargs = {'image': {'required': False}}