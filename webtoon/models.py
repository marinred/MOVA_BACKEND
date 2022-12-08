from django.db import models
from user.models import User

class Webtoon(models.Model):
    platform = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    image_url = models.CharField(max_length=60)
    summary = models.TextField()
    genre = models.CharField(max_length=20)
    day_of_the_week = models.CharField(max_length=10)
    webtoon_link = models.CharField(max_length=100)
    webtoon_bookmarks = models.ManyToManyField(User, related_name="user_bookmarks")
    webtoon_likes= models.ManyToManyField(User, related_name="user_likes")
    
    def __str__(self):
        return (f"{self.platform}, {self.title}")
    
class WebtoonComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE, related_name="webtoon_comment_set")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return (f"{self.user.username}, {self.content}")
