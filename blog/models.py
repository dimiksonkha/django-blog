from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #Additional
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


 
class Post(models.Model):
    title = models.CharField(max_length=250,unique=True)
    content = models.CharField(max_length=1000)
    tag = models.CharField(max_length=100,default='sql')
    category = models.CharField(max_length=150, default='uncategoried')
    featured_img = models.ImageField(upload_to='featured_images', blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    published_date = models.DateTimeField(default=datetime.now())


    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, default=1, related_name='comments')  #have to fix this
    title = models.CharField(max_length=250,blank=True)
    content = models.CharField(max_length=1000, blank=True)
    author = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE,default=1)
    published_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title
