from django.urls import path
from user import views
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib.auth import views as auth_views

app_name = "user"

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile_view'),
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('kakao/login', views.KakaoLoginView.as_view(), name='kakao_login'),
    path('kakao/callback/', views.KakaoCasllbackView.as_view(), name='kakao_callback'),
    path('kakao/login/finish/', views.KakaoLogin.as_view(), name='kakao_login_todjango'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]