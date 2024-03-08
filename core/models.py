from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    profile_pic = models.ImageField(default = 'profiles_pics/default.jpg', upload_to= 'profile_pics')
    bio = models.TextField(max_length=500, null=True , blank=True)