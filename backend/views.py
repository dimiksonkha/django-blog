from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post, Comment, Reply, UserProfileInfo
from blog.forms import UserForm,UserProfileInfoForm, PostForm
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User

# Create your views here.
#@login_required
#Index page with latest posts
def index(request):
    post_list = Post.objects.order_by('published_date')

    paginator = Paginator(post_list, 5) # Show 5 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    my_dict = {'posts':posts}
    return render(request, 'blog/index.html', context=my_dict)


def posts(request):
    post_list = Post.objects.order_by('published_date')

    paginator = Paginator(post_list, 5) # Show 5 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    my_dict = {'posts':posts}
    return render(request, 'backend/posts.html', context=my_dict)
