from django.db import models
from user.models import User
from webtoon.models import Webtoon

class BaseImage(models.Model):
    image = models.ImageField(upload_to='fanart/resize/') # 채색 제거, 크기 조정된 이미지

class FanartImage(models.Model):
    resize_image = models.ForeignKey(BaseImage, on_delete=models.CASCADE)
    hint_image = models.ImageField(upload_to='fanart/hint/') # resize_image에 채색 힌트가 추가된 이미지
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
