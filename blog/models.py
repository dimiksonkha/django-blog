from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250,unique=True)
    content = models.CharField(max_length=1000)
    author = models.CharField(max_length=100, default="xHacker404")
    published_date = models.DateTimeField()


    def __str__(self):
        return self.title



class Comment(models.Model):
    #post = models.ForeignKey(Post)  //have to fix this
    title = models.CharField(max_length=250,unique=True)
    content = models.CharField(max_length=1000)
    author = models.CharField(max_length=100, default="xHacker404")
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
