from django.db import models
from django.contrib.auth.models import AbstractUser

def default_product_image():
    return 'uploadImage/2023/03/defaultAvatar_3.png'


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploadImage/%Y/%m',default=default_product_image,null=True)
    email = models.CharField(max_length=255,unique=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='curentuser')
    video_id = models.IntegerField(null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class ReplyComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)