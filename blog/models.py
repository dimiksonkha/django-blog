from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

# Post Taxonomy:Category
class Category(models.Model):
    text = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.text

# Post Taxonomy:Tag
class Tag(models.Model):
    text = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.text

# Blog Post 
class Post(models.Model):
    title = models.CharField(max_length=250,unique=True)
    content = models.CharField(max_length=1000)
    featured_img = models.ImageField(upload_to='featured_images', blank=True)
    tag = models.ManyToManyField(Tag, related_name='tags')
    category = models.ManyToManyField(Category, related_name='categories')
    status = models.CharField(max_length=100, default='drafted')
    author = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    created_date = models.DateTimeField(default=datetime.now())
    published_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.status = 'published'
        self.published_date = datetime.now()
        self.updated_date = datetime.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(is_approved = True)

    def get_absolute_url(self):
        return reverse('blog:post_details', args=(post_id, ))

    def __str__(self):
        return self.title
