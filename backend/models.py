from django.db import models

# Create your models here.
class BlogSettings(models.Model):
    site_icon = models.ImageField(upload_to='icons')
    site_logo = models.ImageField(upload_to='logos')
    site_title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    post_per_page = models.IntegerField(default=5)
