from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from blog.models import Post
from accounts.models import UserProfileInfo 

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, default=1, related_name='comments')
    content = models.CharField(max_length=1000, blank=True)
    author = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE,default=1)
    created_date = models.DateTimeField(default=datetime.now())
    published_date = models.DateTimeField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)


    def approve(self):
        self.is_approved = True
        self.save()

    def move_to_trash(self):
        self.delete()

    def get_absolute_url(self):
        return reverse('blog:post_details', args=(post_id, ))

    def __str__(self):
        return self.content



class Reply(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE, default=10, related_name='replies')
    content = models.CharField(max_length=1000, blank=True)
    author = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE,default=1)
    published_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title
