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
        
    # def put(self, request, **kwargs): #비밀번호 변경
    #     if kwargs.get('user_id') is None:
    #         return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         user_id = kwargs.get('user_id')
    #         user_object = User.objects.get(id=user_id)
 
    #         update_user_serializer = UserSerializer(user_object, data=request.data)
    #         if update_user_serializer.is_valid():
    #             update_user_serializer.save()
    #             return Response(update_user_serializer.data, status=status.HTTP_200_OK)
    #         else:
    #             return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
            
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
        
#비밀번호 변경       
class ChangePassword(APIView):
    def put(self, request, username, format=None):
        user = request.user
        if user.username == username :
            current_password = request.data.get('current_password',None)
            if current_password is not None:
                password_match = user.check_password(current_password)
                if password_match :
                    new_password = request.data.get('new_password',None)
                    if new_password is not None:
                        user.set_password(new_password)
                        user.save()
                        return Response(status = status.HTTP_200_OK)
                    else :
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                else :
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else :
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else :
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        

#프로필 페이지
class ProfileView(APIView):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        serializer_list = []
        weobtoons = User.objects.get(id=user_id).likes_webtoon.all()
        #weobtoon_serializer = WeobtoonSerializer(webtoons, many=True)
        serializer_user = UserProfileSerializers(user)
        serializer_list.append(serializer_user.data)
        #serializer_list.append(webtoon_serializer.data)
        return Response(serializer_list, status=status.HTTP_200_OK)
#프로필수정
    def put(self, request, user_id):
            user = get_object_or_404(User, id=user_id)
            serializer = UserProfileUpdateSerializers(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

