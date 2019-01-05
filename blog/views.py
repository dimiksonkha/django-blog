from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post, Comment
# Create your views here.

def index(request):
    post_list = Post.objects.order_by('published_date')
    my_dict = {'posts':post_list}
    return render(request, 'blog/index.html', context=my_dict)
