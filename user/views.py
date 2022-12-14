from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from user.models import User
from user.serializers import UserSerializer, CustomObtainPairSerializer,  UserProfileSerializers, UserProfileUpdateSerializers
from django.shortcuts import get_object_or_404
#from webtoon.serializers import WebtoonSerializer

class UserView(APIView):
    #회원가입
    def post(self, request):
        
        if User.objects.filter(email = request.data["email"]):
            return Response({"message" : "이미 가입된 이메일 입니다.\n다시 시도해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        
        
        elif User.objects.filter(username = request.data["username"]):
            return Response({"message" : "이미 가입된 닉네임 입니다.\n다시 시도해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "회원가입을 축하합니다!"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message" : f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        
            
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer
        
#프로필 페이지
class ProfileView(APIView):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer_user = UserProfileSerializers(user)
        return Response(serializer_user.data, status=status.HTTP_200_OK)
    
#프로필 수정  
    def put(self, request):
        print(request.data)
        user = get_object_or_404(User, id=request.user.id)
        serializer = UserProfileUpdateSerializers(user, data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#회원탈퇴
    def delete(self, request):
        user = get_object_or_404(User, id=request.user.id)
        if user.email == request.data["email"]:
            user.delete()
            return Response("성공")
        else:
            return Response("실패")
        