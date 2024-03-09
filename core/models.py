from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    profile_pic = models.ImageField(default='profile_pics/default.jpg',upload_to='profile_pics')
    bio = models.TextField(null=True , blank=True ,max_length=500,default="")

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(max_length=600, null=False)
    date_created = models.DateTimeField(auto_now_add=True,null=False)


    def __str__(self):
        return self.caption
