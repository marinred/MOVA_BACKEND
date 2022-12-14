from django.db import models
from user.models import User
from webtoon.models import Webtoon

# Create your models here.
class BoardCategory(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name


class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE)
    category_name = models.ForeignKey(BoardCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class BoardComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="board_comment_set")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return (f"{self.user.username}, {self.comment}")