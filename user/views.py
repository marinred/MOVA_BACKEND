from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.kakao import views as kakao_view
from user.models import User
from user.serializers import UserSerializer, CustomObtainPairSerializer,  UserProfileSerializers, UserProfileUpdateSerializers
from django.shortcuts import get_object_or_404
import requests
import os
from django.contrib.auth.views import PasswordResetView


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
        user = get_object_or_404(User, id=request.user.id)
        serializer = UserProfileUpdateSerializers(user, data=request.data)
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

# 카카오 소셜로그인
BASE_URL = 	"https://www.chorim.shop/"
KAKAO_CALLBACK_URI = "https://mo-va.site/signup.html"

class KakaoLoginView(APIView):
    def get(self, request):
        client_id = os.environ.get("SOCIAL_AUTH_KAKAO_CLIENT_ID","")
        return Response(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={KAKAO_CALLBACK_URI}&response_type=code&scope=account_email")


class KakaoCasllbackView(APIView):
    def get(self, request):
        client_id = os.environ.get("SOCIAL_AUTH_KAKAO_CLIENT_ID", "")

        code = request.GET.get("code")

        # code로 access token 요청
        token_request = requests.get(f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={KAKAO_CALLBACK_URI}&code={code}")
        token_response_json = token_request.json()

        # 에러 발생 시 중단
        error = token_response_json.get("error", None)
        if error is not None:
            raise Response(error)

        access_token = token_response_json.get("access_token")


        profile_request = requests.post(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()

        kakao_account = profile_json.get("kakao_account")
        email = kakao_account.get("email", None) # 이메일!

        try:
            # 전달받은 이메일로 등록된 유저가 있는지 탐색
            user = User.objects.get(email=email)

            # FK로 연결되어 있는 socialaccount 테이블에서 해당 이메일의 유저가 있는지 확인
            social_user = SocialAccount.objects.get(user=user)

            # 있는데 카카오계정이 아니어도 에러
            if social_user.provider != 'kakao':
                return Response({'err_msg': 'no matching social type'}, status=status.HTTP_400_BAD_REQUEST)

            # 이미 카카오로 제대로 가입된 유저 => 로그인 & 해당 유저의 jwt 발급
            data = {'access_token': access_token, 'code': code}
            accept = requests.post(f"{BASE_URL}user/kakao/login/finish/", data=data)
            accept_status = accept.status_code

            # 뭔가 중간에 문제가 생기면 에러
            if accept_status != 200:
                return Response({'err_msg': 'failed to signin'}, status=accept_status)

            accept_json = accept.json()
            accept_json.pop('user', None)
            return Response(accept_json, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            # 전달받은 이메일로 기존에 가입된 유저가 아예 없으면 => 새로 회원가입 & 해당 유저의 jwt 발급
            data = {'access_token': access_token, 'code': code}
            accept = requests.post(f"{BASE_URL}user/kakao/login/finish/", data=data)
            accept_status = accept.status_code

            # 뭔가 중간에 문제가 생기면 에러
            if accept_status != 200:
                return Response({'err_msg': 'failed to signup'}, status=accept_status)

            accept_json = accept.json()
            accept_json.pop('user', None)
            return Response(accept_json)

class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    callback_url = KAKAO_CALLBACK_URI

class CustomPasswordResetView(PasswordResetView):
    email_template_name = "regist/password_reset_email.html"
    subject_template_name = "regist/password_reset_subject.html"        

