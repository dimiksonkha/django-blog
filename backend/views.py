from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post, Comment, Reply, UserProfileInfo,Tag,Category
from .models import BlogSettings
from blog.forms import UserForm,UserProfileInfoForm, PostForm
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
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

def create_post(request):
    if request.method == 'POST' :
        post_title = request.POST.get('post_title')
        post_content = request.POST.get('post_content')
        featured_img = request.FILES.get('featured_img')
        tag = request.POST.get('tag')
        category = request.POST.get('category')
        status = request.POST.get('status')
        current_user = request.user
        profile = UserProfileInfo.objects.get(user=current_user)

    post = Post()
    post.title = post_title
    post.content = post_content
    post.tag = tag
    post.category = category
    post.featured_img = featured_img
    post.author = User.objects.get(id=current_user.id)

    if status == "Save as Draft":
        post.status = "drafted"
        post.published_date = datetime.now() # Have to remove this line later
    else:
        post.status = "published"


    post.created_date = datetime.now()
    post.updated_date = datetime.now()

    post.save()

    my_dict = {'new_post':'new_post'}
    return render(request, 'backend/posts.html', context=my_dict)

def update_post(request):
    if request.method == 'POST' :
        post_id = request.POST.get('post_id')
        post_title = request.POST.get('post_title')
        post_content = request.POST.get('post_content')
        featured_img = request.FILES.get('featured_img')
        tag = request.POST.get('tag')
        category = request.POST.get('category')
        status = request.POST.get('status')
        current_user = request.user
        profile = UserProfileInfo.objects.get(user=current_user)

    post = Post.objects.get(id=post_id)
    post.title = post_title
    post.content = post_content
    post.tag = tag
    post.category = category
    post.featured_img = featured_img
    post.author = User.objects.get(id=current_user.id)

    if status == "Save as Draft":
        post.status = "drafted"
    else:
        post.status = "published"
        post.published_date = datetime.now()

    post.updated_date = datetime.now()

    post.save()

    my_dict = {'new_post':'new_post'}
    return render(request, 'backend/posts.html', context=my_dict)


#Post edit page
def edit_post(request, pk):
    post = Post.objects.get(id=pk)
    post_tags = post.tag.all()
    other_tags = Category.objects.exclude(post__pk=8)
    post_categories = post.category.all()

    my_dict = {'post':post, 'edit_post':'edit_post', 'post_tags':post_tags, 'other_tags':other_tags, 'post_categories':post_categories}
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

def moderate_comment(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        comment = Comment.objects.get(id=comment_id)
        action = request.POST.get('action')

        if action == "approve":
            comment.approve()

        elif action == "trash":
            comment.move_to_trash()

    return HttpResponseRedirect(reverse('backend:comments'))

def moderate_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        action = request.POST.get('action')

        if action == "admin":
            user.is_superuser = True
            user.save()

        elif action == "moderator":
            user.is_superuser = False
            user.is_staff = True
            user.save()


        elif action == "author":
            user.is_superuser = False
            user.is_staff = False
            user.save()

        elif action == "delete":
            user.delete()

    return HttpResponseRedirect(reverse('backend:users'))

def users(request):
    users = UserProfileInfo.objects.all()
    my_dict = {'users':users}
    return render(request, 'backend/users.html', context=my_dict)

def tags(request):
    tags = Tag.objects.all()
    my_dict = {'taxonomy':'Tag','tags':tags }

    return render(request, 'backend/taxonomy.html', context=my_dict)

def categories(request):
    categories = Category.objects.all()
    my_dict = {'taxonomy':'category', 'categories':categories}

    return render(request, 'backend/taxonomy.html', context=my_dict)

def add_new_tag(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        slug = request.POST.get('slug')
    tag = Tag()
    tag.text = text
    tag.slug = slug
    tag.save()

    my_dict = {'taxonomy':'tag'}
    return render(request, 'backend/taxonomy.html', context=my_dict)



def add_new_category(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        slug = request.POST.get('slug')
    category = Category()
    category.text = text
    category.slug = slug
    category.save()

    my_dict = {'taxonomy':'category'}
    return render(request, 'backend/taxonomy.html', context=my_dict)

def settings(request):

    settings = BlogSettings.objects.get(id=1)
    my_dict = {'settings':settings}
    return render(request, 'backend/settings.html', context=my_dict)



def update_settings(request):
    if request.method == "POST":
        icon = request.FILES.get('icon')
        logo = request.FILES.get('logo')
        title = request.POST.get('title')
        tagline = request.POST.get('tagline')
        keywords = request.POST.get('keywords')
        description = request.POST.get('description')
        post_per_page = request.POST.get('post_per_page')



    settings = BlogSettings.objects.get(id=1)

    settings.site_icon = icon
    settings.site_logo = logo
    settings.site_title = title
    settings.tagline = tagline
    settings.keywords = keywords
    settings.description = description
    settings.post_per_page = post_per_page
    settings.save()

    return HttpResponseRedirect(reverse('backend:settings'))

def profile(request):
    profile = UserProfileInfo.objects.get(user=request.user)
    my_dict = {'profile':profile}
    return render(request, 'backend/profile.html', context=my_dict)

def update_profile(request):

    if request.method == "POST":
        profile_id = request.POST.get('profile_id')
        pic = request.FILES.get('profile_pic')
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

    profile = UserProfileInfo.objects.get(id=profile_id)
    profile.profile_pic = pic
    profile.save()

    user = request.user
    user.username = username
    user.first_name = firstname
    user.last_name = lastname
    user.email = email
    if password :
        user.set_password(password)

    update_session_auth_hash(request, request.user)
    user.save()


    return HttpResponseRedirect(reverse('backend:profile'))
