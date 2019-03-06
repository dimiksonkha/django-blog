from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.http import HttpResponse
from blog.models import Post,Tag,Category
from accounts.models import UserProfileInfo
from comments.models import Comment,Reply
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User


# Create your views here.

#Index page with latest posts
def index(request):
    post_list = Post.objects.filter(status='published').order_by('published_date')

    paginator = Paginator(post_list, 5) # Show 5 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    my_dict = {'posts':posts}
    return render(request, 'blog/index.html', context=my_dict)

#Post details page
def post_details(request, pk):
    post = get_object_or_404(Post, id=pk)
    post_tags = post.tag.all()
    post_categories = post.category.all()

    next_posts = Post.objects.filter(published_date__gt=post.published_date)
    if(next_posts):
        next_post = next_posts [0]
    else:
        next_post = None

    previous_posts = Post.objects.filter(published_date__lt=post.published_date)
    if(previous_posts):
        previous_post = previous_posts [previous_posts.count()-1]
    else:
        previous_post = None

    post_id = post.id
    comments = post.comments.filter(is_approved=True)



    my_dict = {
        'post_tags': post_tags,
        'post_categories': post_categories,
        'post': post,
        'comments': comments,
        'next_post': next_post,
        'previous_post': previous_post
    }

    return render(request, 'blog/single.html', context=my_dict)


def custom_500(request):
    return render(request, '500.html', status=500)


def custom_400(request):
    return render(request, '400.html', status=400)


def custom_403(request):
    return render(request, '403.html', status=403)


#All posts by published year
def archeive_posts(request, year):
    post_list = Post.objects.filter(published_date__year = year)

    paginator = Paginator(post_list, 5) # Show 5 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {'year':year,'posts':posts}
    return render(request, 'blog/archeive.html', context)

#All posts by post tag
def archeive_posts_by_tag(request, tag):
    tag = get_object_or_404(Tag, text=tag)
    post_list = tag.tags.all()

    paginator = Paginator(post_list, 5) # Show 5 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {'posts':posts}
    return render(request, 'blog/archeive.html', context)

#All posts by post category
def archeive_posts_by_category(request, category):
    category = get_object_or_404(Category, text=category)
    post_list = category.categories.all()
    paginator = Paginator(post_list, 5) # Show 5 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {'posts':posts}
    return render(request, 'blog/archeive.html', context)

#All posts by a specific author
def archeive_posts_by_author(request, username):
    author = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author=author.id)

    paginator = Paginator(post_list, 5) # Show 5 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {'posts':posts}
    return render(request, 'blog/archeive.html', context)

#All posts by published_date
def archeive_posts_by_date(request, year, month, day):
    post_list = Post.objects.filter(published_date__year=year, published_date__month=month, published_date__day=day)

    paginator = Paginator(post_list, 5) # Show 5 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {'posts':posts}
    return render(request, 'blog/archeive.html', context)

#Search Result
def search_view(request):
        if request.method == 'GET' :
            search_query = request.GET.get('search_box')
            tag_list = Tag.objects.filter(text__contains=search_query)
            cat_list = Category.objects.filter(text__contains=search_query)
            post_list = Post.objects.filter(title__contains=search_query ).distinct() | Post.objects.filter(content__contains=search_query ).distinct() | Post.objects.filter(tag__id__in=tag_list).distinct() | Post.objects.filter(category__id__in=cat_list).distinct()

        paginator = Paginator(post_list, 5) # Show 5 posts per page
        page = request.GET.get('page')
        posts = paginator.get_page(page)

        context = {'posts':posts}

        return render(request, 'blog/archeive.html', context)
