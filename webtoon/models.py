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
    webtoon_bookmarks = models.ManyToManyField(User)
    webtoon_likes= models.ManyToManyField(User)