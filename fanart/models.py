from django.db import models
from user.models import User
from webtoon.models import Webtoon
import os
from uuid import uuid4

# image uuid로 저장
class UploadTo:
    def __init__(self, folder = None):
        self.folder = folder
    def save_path(self, instance, filename):
        uuid = f"{uuid4().hex}.png"
        return f"fanart/{self.folder}/{uuid}"

class BaseImage(models.Model):
    image = models.ImageField(upload_to='fanart/resize/') # 채색 제거, 크기 조정된 이미지

class FanartImage(models.Model):
    resize_image = models.ForeignKey(BaseImage, on_delete=models.CASCADE)
    hint_image = models.ImageField(upload_to=UploadTo(folder='hint').save_path) # resize_image에 채색 힌트가 추가된 이미지
    result_image = models.ImageField(upload_to='fanart/result/') # 채색 완료된 이미지

class Fanart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField() # 그림 설명
    image = models.ForeignKey(FanartImage, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,related_name='user_likes')
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FanartComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fanart = models.ForeignKey(Fanart, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
