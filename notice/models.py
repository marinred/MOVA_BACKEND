from django.db import models
from user.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return (self.category_name)
    


class Notice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notice_category_set')
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
