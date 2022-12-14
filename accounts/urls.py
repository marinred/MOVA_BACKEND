from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.LoginMove, name='login_view'),
]