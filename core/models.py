from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    profile_pic = models.ImageField(default='profile_pics/default.jpg',upload_to='profile_pics')
    bio = models.TextField(null=True , blank=True ,max_length=500,default="")

    def get_num_posts(self):
        return Post.objects.filter(user=self).count()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(max_length=600, null=False)
    date_created = models.DateTimeField(auto_now_add=True,null=False)


    def __str__(self):
        return self.caption


class Friends(models.Model):
    user_A = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='user_A')
    user_B = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='user_B')

    def __str__(self):
        return self.user_A.username + "  ---  " + self.user_B.username

