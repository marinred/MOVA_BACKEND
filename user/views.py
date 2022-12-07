from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from user.models import User
from user.serializers import UserSerializer, CustomObtainPairSerializer,  UserProfileSerializers, UserProfileUpdateSerializers
from django.shortcuts import get_object_or_404
#from webtoon.serializers import WebtoonSerializer

class UserView(APIView):
    def post(self, request): #회원가입
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "가입완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message" : f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        
    # def delete(self, request, **kwargs): #회원탈퇴
    #     if kwargs.get('user_id') is None:
    #         return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         user_id = kwargs.get('user_id')
    #         user_object = User.objects.get(id=user_id)
    #         user_object.delete()
    #         return Response("test ok", status=status.HTTP_200_OK)
            
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer
        

#프로필 페이지
class ProfileView(APIView):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer_user = UserProfileSerializers(user)
        return Response(serializer_user.data, status=status.HTTP_200_OK)
    
#프로필수정
    def put(self, request):
            user = get_object_or_404(User, id=request.user.id)
            serializer = UserProfileUpdateSerializers(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

