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

    my_dict = {'posts':posts, 'post_page':'post_page'}
    return render(request, 'backend/posts.html', context=my_dict)

def new_post(request):
    my_dict = {'new_post':'new_post'}
    return render(request, 'backend/posts.html', context=my_dict)

#Post edit page
def edit_post(request, pk):
    post = Post.objects.get(id=pk)

    my_dict = {'post':post, 'edit_post':'edit_post'}
    return render(request, 'backend/posts.html', context=my_dict)

# Post Delete View
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()

    return HttpResponseRedirect(reverse('backend:posts'))

def comments(request):
    comments = Comment.objects.all();
    my_dict = {'comments':comments}

    return render(request, 'backend/comments.html', context=my_dict)

def users(request):
    users = UserProfileInfo.objects.all()
    my_dict = {'users':users}
    return render(request, 'backend/users.html', context=my_dict)

def tags(request):
    my_dict = {'taxonomy':'Tag'}

    return render(request, 'backend/taxonomy.html', context=my_dict)

def categories(request):
    my_dict = {'taxonomy':'Category'}

    return render(request, 'backend/taxonomy.html', context=my_dict)

def settings(request):

    return render(request, 'backend/settings.html')

def profile(request):

    return render(request, 'backend/profile.html')
